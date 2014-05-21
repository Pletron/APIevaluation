import os
from commands import getoutput

output = {}
def send_request(image_directory):
    result = getoutput('br -algorithm GenderEstimation -enroll %s terminal.csv'%image_directory)

    if result.find("command not found") > -1:
        output['status'] = "command not found"
    else:
        output['status'] = "success"


    return output