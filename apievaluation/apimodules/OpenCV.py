import time
from apievaluation.apitools.ExternalProc import ExternalProc
from apievaluation.apitools.database import Database
import settings

output = {}
def send_request(image_directory, process=None):
    proc = process.process
    print "New openCV thread"
    db = Database('OpenCV')
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
        face = {}
        face['Face_topLeft_X'] = float(res[headers.index('Face_topLeft_X')])
        face['Face_topLeft_Y'] = float(res[headers.index('Face_topLeft_Y')])
        face['Face_bottomRight_X'] = float(res[headers.index('Face_bottomRight_X')])
        face['Face_bottomRight_Y'] = float(res[headers.index('Face_bottomRight_Y')])
        output['face'].append({'gender':res[headers.index('Gender')],'face':face})

        db.add_image(output['status'],image,output['execution_time'],face['Face_topLeft_X'],face['Face_topLeft_Y'],face['Face_bottomRight_X'],face['Face_bottomRight_Y'],res[headers.index('Gender')],-1,-1,-1)

    return output



def start_module():
    cmd = '%s/libraries/OpenCV/OpenCV %s/libraries/OpenCV/trained.xml' % (settings.MODULES_DIR,settings.MODULES_DIR)
    p = ExternalProc(arg_list=cmd)
    p.process.expect('Algorithm loaded')
    return p