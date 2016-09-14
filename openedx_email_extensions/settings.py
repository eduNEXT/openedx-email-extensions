# -*- coding: utf-8 -*-
"""
This is the settings file for the openedx_email_extensions application
"""

from path import Path as path


APP_ROOT = path(__file__).abspath().dirname()

ENABLE_MULTIPART_EMAIL = True
COMPATIBILITY = {
    "registration/password_reset_email.html": "password_reset_email_html.html",
}

TEMP_PATH = '/edx/src/openedx-email-extensions/openedx_email_extensions/templates'
