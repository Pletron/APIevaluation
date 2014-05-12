import urllib2,urllib
import time
from apievaluation.apimodules.lib.facepp import File, APIError
from apievaluation.apimodules.lib.facepp import API

URL = 'https://apius.faceplusplus.com/v2/'
API_KEY = 'e0058e5bd626d7fd9b5151be643035e1'
API_SECRET = 'Ochu_1o1DFtaUA6brGQzOQ-vARsGXf1I'
EXAMPLE_IMAGE = urllib.quote_plus('http://faceplusplus.com/static/img/demo/8.jpg')
TIMEOUT = 10


def send_request(image_directory):


    start_time = time.time()
    try:
        api = API(key=API_KEY, secret=API_SECRET, srv=URL, timeout=TIMEOUT, max_retries=0, retry_delay=0)
        json_result = api.detection.detect(img = File(image_directory))
        execution_time = time.time() - start_time

        json_result['execution_time'] = execution_time
        json_result['status'] = 'success'

        if len(json_result['face']) > 0:
            json_result['status'] = 'success'
        else:
            json_result['status'] = 'no detection'

        return json_result
    except urllib2.URLError:
        return {'status' : 'timeout'}
    except APIError as e:
        execution_time = time.time() - start_time
        return {'execution_time' : execution_time, 'status' : {'error':{'code':e.code, 'url':e.url}}}

