"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from __future__ import absolute_import, unicode_literals

from os.path import join, abspath, dirname


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'openedx_email_extensions',
)

LOCALE_PATHS = [
    root('openedx_email_extensions', 'conf', 'locale'),
]

MIDDLEWARE_CLASSES = tuple()

ROOT_URLCONF = 'openedx_email_extensions.urls'

SECRET_KEY = 'insecure-secret-key'

FEATURES = {
    "ENABLE_MULTIPART_EMAIL": True,
}
