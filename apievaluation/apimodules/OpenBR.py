from _ctypes import sizeof
import io
import time
import select
import os
from apievaluation.apitools.ExternalProc import ExternalProc
from apievaluation.apitools.database import Database
import settings

output = {}
def send_request(image_directory, process=None):
    proc = process.process
    print "New openBR thread"
    db = Database('OpenBR')
    image = image_directory.split("/")
    image = image[len(image)-1]

    start_time = time.time()
    proc.sendline(image_directory)
    proc.expect("end of result")
    execution_time = time.time() - start_time
    results = proc.before
    results = results.replace('\r','').split("\n")

    if results[0] == '':
        results.pop(0)
    results.pop(0)
    results.pop(len(results)-1)



    headers = results[0].split(',')
    results.pop(0)
    output['execution_time'] = execution_time

    if len(results) == 0:
        output['status'] = 'no faces'
    else:
        output['status'] = 'success'

    output['face'] = []
    for res in results:
        res = res.split(',')
        eyeLeft = {}
        eyeRight = {}
        eyeLeft['X'] = float(res[headers.index('First_Eye_X')])
        eyeLeft['Y'] = float(res[headers.index('First_Eye_Y')])
        eyeRight['X'] = float(res[headers.index('Second_Eye_X')])
        eyeRight['Y'] = float(res[headers.index('Second_Eye_Y')])
        output['face'].append({'gender':res[headers.index('Gender')],'confidence':float(res[headers.index('Confidence')]),'left_eye':eyeLeft,'right_eye':eyeRight})

        db.add_image(output['status'],image,output['execution_time'],res[headers.index('Gender')],-1,-1,res[headers.index('Confidence')])

    return output



def start_module():
    cmd = '%s/libraries/OpenBR' % settings.MODULES_DIR
    p = ExternalProc(arg_list=cmd)
    p.process.expect('Algorithm loaded')
    return p