import os
from commands import getoutput


def send_request(image_directory):
    result = getoutput('br -algorithm GenderEstimation -enroll %s terminal.csv'%image_directory)
    pass