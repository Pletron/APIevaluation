"""Main test class for APIevaluation"""

import os
from apievaluation import apievaluation
from apievaluation.apimodules import ReKognition, FacePlusPlus, OpenBR, OpenCV
from apievaluation.apitools import tools
import settings

TEST_IMAGES_DIR = os.path.join(settings.ROOT_DIR, "tests/res")


class TestAPIevaluationBase(object):

    def test_get_API_results(self):
        json_result = apievaluation.get_API_results(image_directory=TEST_IMAGES_DIR)
        assert len(json_result) > 0





class TestToolsBase(object):

    def test_base64(self):
        assert len(tools.base64_convert(TEST_IMAGES_DIR+'/2003.jpg')) > 50

    def test_load_module(self):
        mod = tools.load_module(os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0], 'apievaluation/apimodules/ReKognition.py'))
        assert hasattr(mod,"get_Data")



class TestReKognitionBase(object):

    def test_url(self):
        assert len(ReKognition.get_Data(TEST_IMAGES_DIR+'/2003.jpg')) == 4

    def test_send_request(self):
        json_result = ReKognition.send_request(TEST_IMAGES_DIR+'/2003.jpg')
        assert json_result['status'] == 'success'


class TestFacePP(object):

    def test_send_request(self):
        json_result = FacePlusPlus.send_request(TEST_IMAGES_DIR+'/2003.jpg')
        assert json_result['status'] == 'success'

class TestOpenBR(object):

    def test_send_request(self):
        proc = OpenBR.start_module()
        json_result = OpenBR.send_request(TEST_IMAGES_DIR+'/2003.jpg',proc)
        assert json_result['status'] == 'success'

class TestOpenCV(object):

    def test_send_request(self):
        proc = OpenCV.start_module()
        json_result = OpenCV.send_request(TEST_IMAGES_DIR+'/2003.jpg',proc)
        assert json_result['status'] == 'success'