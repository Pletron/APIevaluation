import random
from threading import Thread
import time
import shutil
import settings
import os
from apitools import tools


TEST_IMAGES_DIR = os.path.join(settings.ROOT_DIR, "tests/res/images")


def initiate_test(noImages, mode, isDirectory):
    if isDirectory:
        json_result = get_API_results(images_number=noImages, image_directory=mode)
    elif mode == "test":
        json_result = get_API_results(images_number=noImages, image_directory=TEST_IMAGES_DIR)
    elif mode == "desktop":
        json_result = get_API_results(images_number=noImages, image_directory='/home/ubuntu/Desktop/')
    else:
        json_result = get_API_results(images_number=noImages)
    return json_result


output = {}


def get_API_results(image_directory=settings.IMAGES_DIR, modules_directory=settings.MODULES_DIR, images_number=-1):
    """
    Initializes the data extracting for each API
    """
    processes = {}
    for filename in os.listdir(modules_directory):
        if filename.find("__init__") < 0 and filename.find(".pyc") < 0 and filename != "libraries":
            mod = tools.load_module("%s/%s" % (modules_directory, filename))
            if hasattr(mod, 'start_module'):
                processes[filename] = mod.start_module()
                print "Started %s" % filename
            else:
                processes[filename] = None

    images = []
    for image in os.listdir(image_directory):
        if image.find(".jpg") >= 0 or image.find(".png") >= 0 or image.find(".gif") >= 0:
            images.append(image)


    random.shuffle(images)
    iteration = 0
    for image in images:

        start_time = time.time()


        output[image] = {}
        threads = []
        for filename in os.listdir(modules_directory):
            if filename.find("__init__") < 0 and filename.find(
                    ".pyc") < 0 and filename != "libraries":
                        t = Thread(target=request_thread, args=(filename, image_directory, modules_directory, image, processes[filename]))
                        threads.append(t)

        try:
            [x.start() for x in threads]
            [x.join() for x in threads]
        except:
            print "Error: unable to start thread"

        print "%d Took %f seconds to process \"%s\"" % (iteration,time.time() - start_time, image)
        iteration += 1
        shutil.move("%s/%s" % (image_directory, image), "/home/ubuntu/Documents/checked_images/%s" % image)
        if iteration == images_number and images_number != -1:
            break

    return output




def request_thread(filename, image_directory, modules_directory, image, process):
    name = filename.replace(".py", "")
    mod = tools.load_module("%s/%s" % (modules_directory, filename))
    if process is None:
        result = mod.send_request("%s/%s" % (image_directory, image))
    else:
        result = mod.send_request("%s/%s" % (image_directory, image), process)
    output[image][name] = result