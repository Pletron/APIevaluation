import os
from commands import getoutput
import time
from apievaluation.apitools.database import Database

output = {}
def send_request(image_directory):
    db = Database('OpenBR')
    image = image_directory.split("/")
    image = image[len(image)-1]

    start_time = time.time()
    result = getoutput('br -algorithm GenderEstimation -enroll %s terminal.csv'%image_directory)
    execution_time = time.time() - start_time

    if result.find("command not found") > -1:
        output['status'] = "command not found"
    else:
        output['status'] = "success"
        output['execution_time'] = execution_time
        result = result.split('\n')

        for x in range(0, 4):
            result.pop(0)

        headers = result[0].split(',')
        result.pop(0)

        for res in result:
            res = res.split(',')
            output['gender'] = res[headers.index('Gender')]
            output['confidence'] = res[headers.index('Confidence')]
            output['left_eye'] = {}
            output['right_eye'] = {}
            output['left_eye']['X'] = res[headers.index('First_Eye_X')]
            output['left_eye']['Y'] = res[headers.index('First_Eye_Y')]
            output['right_eye']['X'] = res[headers.index('Second_Eye_X')]
            output['right_eye']['Y'] = res[headers.index('Second_Eye_Y')]
            print "The Gender is: %s" % res[headers.index('Gender')]
            print "The Confidence is: %s" % res[headers.index('Confidence')]
            db.add_image(output['status'],image,output['execution_time'],output['gender'],-1,-1,output['confidence'])





    return output