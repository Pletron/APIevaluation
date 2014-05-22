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
    db = Database('OpenBR')
    image = image_directory.split("/")
    image = image[len(image)-1]

    start_time = time.time()
    process.write_handle(input=image_directory)
    results = []
    while 1:
        ready, _, _ = select.select([process.master], [], [], 0.4)
        if ready:
            data = os.read(process.master, 512)
            if not data:
                break
            if data.rstrip() != 'end of result':
                results.append(data.rstrip())
            else:
                break
        elif process.process.poll() is not None: # select timeout
            break # proc exited

    execution_time = time.time() - start_time

    headers = results[0].split(',')
    results.pop(0)
    output['execution_time'] = execution_time

    if len(results) == 0:
        output['status'] = 'no faces'
    else:
        output['status'] = 'sucess'

    output['face'] = []
    for res in results:
        output['face'].append({'gender':res[headers.index('Gender')]})


    return output



def start_module():
    cmd = '%s/libraries/OpenBR' % settings.MODULES_DIR
    p = ExternalProc(arg_list=cmd)
    while True:
        if p.stdout.readline().find('Algorithm loaded') > -1:
            break
    return p