import urllib
import requests
import time
from apievaluation.apitools import tools

URL = 'https://rekognition.com/func/api/'
API_KEY = '4HxkCzeWAtPyrsyt'
API_SECRET = 'lP2bp9lEJCE5a815'
JOBS = {'face_gender'}
EXAMPLE_IMAGE = urllib.quote_plus('http://rekognition.com/static/img/people.jpg')
TIMEOUT = 10


def send_request(image_directory):

    start_time = time.time()

    try:
        r = requests.post(URL, data=get_Data(image_directory), timeout=TIMEOUT)
        execution_time = time.time() - start_time

        json_result = r.json()
        json_result['execution_time'] = execution_time

        if len(json_result['face_detection']) > 0:
            json_result['status'] = 'success'
        else:
            json_result['status'] = 'no detection'

        return json_result
    except requests.exceptions.Timeout:
        return {'status' : 'timeout'}




def get_Data(image_directory):
    if image_directory != '':
        raw_image = tools.base64_convert(image_directory)
        return {'base64':raw_image,  'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS}
    else:
        return {'urls':EXAMPLE_IMAGE,'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS}