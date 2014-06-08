import urllib
import requests
import time
from apievaluation.apitools import tools
from apievaluation.apitools.database import Database

URL = 'https://www.rekognition.com/func/api/'
API_KEY = 'JzBQLsVp1751bk1H'
API_SECRET = '4GlPbkg3vnJKUR6H'
JOBS = 'face_gender_age_aggressive_place'
EXAMPLE_IMAGE = urllib.quote_plus('http://rekognition.com/static/img/people.jpg')
TIMEOUT = 10


def send_request(image_directory):
    db = Database("ReKognition")
    image = image_directory.split("/")
    image = image[len(image)-1]
    start_time = time.time()

    try:
        r = requests.post(URL, data=get_Data(image_directory), timeout=TIMEOUT)
        execution_time = time.time() - start_time

        json_result = r.json()
        json_result['execution_time'] = execution_time

        if len(json_result['face_detection']) > 0:
            json_result['status'] = 'success'
            for face in json_result['face_detection']:
                gender = 'Male' if float(face['sex']) > 0.5 else 'Female'
                gender_accuracy =  abs(face['sex']-0.5)*200
                age = face['age']
                confidence = face['confidence']
                topLeft_X = face['boundingbox']['tl']['x']
                topLeft_Y = face['boundingbox']['tl']['y']
                bottomRight_X = topLeft_X+face['boundingbox']['size']['width']
                bottomRight_Y = topLeft_Y+face['boundingbox']['size']['height']
                db.add_image("success",image,json_result['execution_time'], topLeft_X,topLeft_Y,bottomRight_X,bottomRight_Y,gender, gender_accuracy, age, confidence)
        else:
            json_result['status'] = 'no detection'
            db.add_image("no detection",image,json_result['execution_time'], -1, -1, -1, -1)

        # db.save()


        return json_result
    except requests.exceptions.Timeout:
        execution_time = time.time() - start_time
        db.add_image("timeout",image,execution_time, -1, -1, -1, -1)
        return {'status' : 'timeout'}





def get_Data(image_directory):
    if image_directory != '':
        raw_image = tools.base64_convert(image_directory)
        return {'base64':raw_image,  'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS}
    else:
        return {'urls':EXAMPLE_IMAGE,'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS}