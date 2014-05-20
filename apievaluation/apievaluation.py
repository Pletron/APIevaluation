import json
from threading import Thread
import time
import settings
import os
from apitools import tools


TEST_IMAGES_DIR = os.path.join(settings.ROOT_DIR, "tests/res/images")


def initiate_test(noImages, test):
    if test:
        json_result = get_API_results(images_number=noImages, image_directory=TEST_IMAGES_DIR)
    else:
        json_result = get_API_results(images_number=noImages)
    return json_result


output = {}


def get_API_results(image_directory=settings.IMAGES_DIR, modules_directory=settings.MODULES_DIR, images_number=-1):
    """
    Initializes the data extracting for each API
    """

    iteration = 0
    for image in os.listdir(image_directory):
        if image.find(".DS_Store") < 0:
            start_time = time.time()

            output[image] = {}
            threads = []
            for filename in os.listdir(modules_directory):
                if filename.find("__init__") < 0 and filename.find(
                        ".pyc") < 0 and filename != "apis":
                    t = Thread(target=request_thread, args=(filename, image_directory, modules_directory, image))
                    threads.append(t)

            try:
                [x.start() for x in threads]
                [x.join() for x in threads]
            except:
                print "Error: unable to start thread"

            print "Took %f seconds to process \"%s\"" % (time.time() - start_time, image)
            iteration += 1
            if iteration == images_number and images_number != -1:
                break

    return output




def request_thread(filename, image_directory, modules_directory, image):
    name = filename.replace(".py", "")
    mod = tools.load_module("%s/%s" % (modules_directory, filename))
    result = mod.send_request("%s/%s" % (image_directory, image))
    output[image][name] = result