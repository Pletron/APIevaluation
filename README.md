APIevaluation
=============

Face recognition evaluation framework.
Only tested for Ubuntu 13.04.

Installation
=============
Note that OpenBR must be installed and built for the OpenBR module to work.
Installation instructions for OpenBR can be found here: 

 - http://openbiometrics.org/doxygen/latest/installation.html

To install the APIevaluation project make sure to have python-setuptools, python-dev and mysql_config available and installed:

 - sudo apt-get install python-setuptools python-dev libmysqlclient-dev

Installation instructions:

 1. python setup.py build (In the root project folder)
 2. python setup.py install