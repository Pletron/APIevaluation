"""Main test class for APIevaluation"""

import os
import shutil
import json
import datetime

from apievaluation import app

class TestSandmanBase(object):
    """Base class for all APIevaluation test classes."""