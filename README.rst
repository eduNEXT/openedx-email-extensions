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
