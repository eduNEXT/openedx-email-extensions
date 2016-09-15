A package by `eduNEXT`__.

__ http://www.edunext.co/

openedx-email-extensions  |Travis|_ |Codecov|_
===================================================
.. |Travis| image:: https://travis-ci.org/edx/openedx-email-extensions.svg?branch=master
.. _Travis: https://travis-ci.org/edx/openedx-email-extensions

.. |Codecov| image:: http://codecov.io/github/edx/openedx-email-extensions/coverage.svg?branch=master
.. _Codecov: http://codecov.io/github/edx/openedx-email-extensions?branch=master

A package to make the outgoing emails in open-edx good looking.

Overview
--------

This django application is to be used together with the openedx platform. It
makes it easy for a fork administrator to convert outgoing emails to a multipart
format that support both text and html.

How to install
--------------
```
git clone https://github.com/eduNEXT/openedx-email-extensions.git
cd openedx-email-extensions/
mkdir ../VENVS
virtualenv ../VENVS/openedx-email-extensions
source ../VENVS/openedx-email-extensions/bin/activate
make requirements
```

How to run for dev
------------------
./manage.py render_templates

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.


 1993  git add .
 1994  git commit -m "First commit, fresh from the cookie cutter"
 1995  cd src/openedx-email-extensions/
 1996  git remote add origin https://github.com/eduNEXT/openedx-email-extensions.git
 1997  git push -u origin master
 1998  cd ../..
 1999  vagrant ssh
 2000  cd src/openedx-email-extensions/
 2001  mkdir ../VENVS
 2002  virtualenv ../VENVS/emailext
 2003  source ../VENVS/emailext/bin/activate
 2004  make pip-compile
 2005  pip install --upgrade pip
 2006  make pip-compile
 2007  pip-compile --upgrade -o requirements/base.txt requirements/base.in
 2008  ll
 2009  ./manage.py test
 2010  make pip-compile
 2011  make requirements
 2012  py.test
 2013  ./manage.py render_templates
 2014  make requirements 
 2015  make pip-compile 
 2016  make requirements 
 2017  ./manage.py render_templates
 2018  pip install mock
 2019  ./manage.py render_templates
 2020  history
