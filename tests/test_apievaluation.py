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
        assert ReKognition.get_URL('') == 'https://rekognition.com/func/api/?api_key=4HxkCzeWAtPyrsyt&api_secret=lP2bp9lEJCE5a815&jobs=face_part&urls=http%3A%2F%2Frekognition.com%2Fstatic%2Fimg%2Fpeople.jpg'


    def test_base64(self):
        base64_image = ReKognition.base64_convert(os.path.dirname(os.path.realpath(__file__))+'/test_images/people.jpg')
        assert len(base64_image) > 25000