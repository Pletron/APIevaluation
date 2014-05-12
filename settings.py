import os

ROOT_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(ROOT_DIR, "res/images")
MODULES_DIR = os.path.join(ROOT_DIR, "apievaluation/apimodules")

class Settings(object):



    def __init__(self, images_dir, modules_dir):
        self.IMAGES_DIR = images_dir
        self.MODULES_DIR = modules_dir