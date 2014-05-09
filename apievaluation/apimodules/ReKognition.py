import base64
import json
import urllib

REQUEST_URL = 'https://rekognition.com/func/api/?api_key=%s&api_secret=%s&jobs=%s&urls=%s'
API_KEY = '4HxkCzeWAtPyrsyt'
API_SECRET = 'lP2bp9lEJCE5a815'
JOBS = 'face_part'
EXAMPLE_IMAGE = urllib.quote_plus('http://rekognition.com/static/img/people.jpg')


def send_request(image_directory):

    # base64_image = base64_convert(image_directory)
    return (REQUEST_URL % (API_KEY,API_SECRET,JOBS, EXAMPLE_IMAGE))


def base64_convert(image_directory):
    with open(image_directory, "rb") as image:
        image_data = image.read()
        return image_data.encode("base64")

def get_URL(image_directory):
    if image_directory != '':
        base64_image = base64_convert(image_directory)
        return (REQUEST_URL % (API_KEY,API_SECRET,JOBS, base64_image))
    else:
        return (REQUEST_URL % (API_KEY,API_SECRET,JOBS, EXAMPLE_IMAGE))