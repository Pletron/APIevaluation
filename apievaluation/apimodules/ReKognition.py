import urllib
import requests
import time

URL = 'https://rekognition.com/func/api/'
API_KEY = '4HxkCzeWAtPyrsyt'
API_SECRET = 'lP2bp9lEJCE5a815'
JOBS = 'face_part'
EXAMPLE_IMAGE = urllib.quote_plus('http://rekognition.com/static/img/people.jpg')
TIMEOUT = 10


def send_request(image_directory):

    start_time = time.time()

    try:
        r = requests.post(URL, data=get_Data(image_directory), timeout=TIMEOUT)
        end_time = time.time() - start_time
        json_result = r.json()
        json_result['execution_time'] = end_time
        return json_result
    except requests.exceptions.Timeout as d:
        return {'execution_time' : -1}



def base64_convert(image_directory):
    with open(image_directory, "rb") as image:
        image_data = image.read()
        return image_data.encode("base64")


def get_Data(image_directory):
    if image_directory != '':
        base64_image = base64_convert(image_directory)
        return {'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS, 'base64':base64_image}
    else:
        return {'api_key':API_KEY, 'api_secret':API_SECRET, 'jobs':JOBS, 'urls':EXAMPLE_IMAGE}