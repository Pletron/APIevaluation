"""Main test class for APIevaluation"""

from apievaluation.apimodules import ReKognition
import os


class TestAPIevaluationBase(object):
    @staticmethod
    def is_html_response(response):
        """Return True if *response* is an HTML response"""
        assert 'text/html' in str(response.headers['Content-type'])
        return '<!DOCTYPE html>' in response.get_data(as_text=True)

class TestReKognitionBase(object):
    """Base class for all APIevaluation test classes."""

    def test_url(self):
        assert len(ReKognition.get_Data(os.path.dirname(os.path.realpath(__file__))+'/test_images/people.jpg')) == 4


    def test_base64(self):
        base64_image = ReKognition.base64_convert(os.path.dirname(os.path.realpath(__file__))+'/test_images/people.jpg')
        assert len(base64_image) > 25000

    def test_send_request(self):
        json_result = ReKognition.send_request(os.path.dirname(os.path.realpath(__file__))+'/test_images/people.jpg')
        assert json_result['execution_time'] > 0