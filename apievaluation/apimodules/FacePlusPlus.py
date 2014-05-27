import urllib
import time
from apievaluation.apimodules.libraries.facepp import File
from apievaluation.apimodules.libraries.facepp import API
from apievaluation.apitools.database import Database

URL = 'https://apius.faceplusplus.com/v2/'
API_KEY = 'e0058e5bd626d7fd9b5151be643035e1'
API_SECRET = 'Ochu_1o1DFtaUA6brGQzOQ-vARsGXf1I'
EXAMPLE_IMAGE = urllib.quote_plus('http://faceplusplus.com/static/img/demo/8.jpg')
TIMEOUT = 5


def send_request(image_directory):
    db = Database("FacePlusPlus")
    image = image_directory.split("/")
    image = image[len(image)-1]

    start_time = time.time()
    try:
        api = API(key=API_KEY, secret=API_SECRET, srv=URL, timeout=TIMEOUT, max_retries=0, retry_delay=0)
        json_result = api.detection.detect(img = File(image_directory))
        execution_time = time.time() - start_time

        json_result['execution_time'] = execution_time
        json_result['status'] = 'success'

        if len(json_result['face']) > 0:
            json_result['status'] = 'success'
            for face in json_result['face']:
                gender = face['attribute']['gender']['value']
                gender_accuracy = face['attribute']['gender']['confidence']
                age = face['attribute']['age']['value']
                db.add_image("success",image,json_result['execution_time'], gender, gender_accuracy, age, -1)
        else:
            json_result['status'] = 'no detection'
            db.add_image("no detection", image,json_result['execution_time'], -1, -1, -1, -1)

        # db.save()
        return json_result
    except Exception as e:
        execution_time = time.time() - start_time
        db.add_image("error", image,execution_time, -1, -1, -1, -1)
        print "Face plus plus exception:"
        print e
        return {'execution_time' : execution_time, 'status' : {'error':'Exception'}}
