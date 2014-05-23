from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import apievaluation

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

# long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='APIevaluation',
    version=apievaluation.__version__,
    packages = find_packages(),
    url='http://github.com/Pletron/APIevaluation/',
    license='MIT License',
    author='Philip Masek',
    tests_require=['pytest'],
    install_requires=['requests>=2.2.1',
                      'MySQL-python==1.2.5',
                      'pexpect'
                    ],
    cmdclass={'tests': PyTest},
    author_email='philip.masek@gmail.com',
    description="Framework for evaluating face recognition APIs",
    # long_description=long_description,
    include_package_data=True,
    platforms='any',
    scripts = ['start_evaluation.py'],
    test_suite='apievaluation.tests.test_apievaluation',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)