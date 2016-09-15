# -*- coding: utf-8 -*-
"""
This is the settings file for the openedx_email_extensions application
"""

from path import Path as path
from django.conf import settings

APP_ROOT = path(__file__).abspath().dirname()
REPO_ROOT = APP_ROOT.dirname()
TEMPLATES_PATH =  APP_ROOT / 'templates'

ENABLE_MULTIPART_EMAIL = settings.FEATURES.get('ENABLE_MULTIPART_EMAIL', False)
COMPATIBILITY = {
    "registration/password_reset_email.html": "password_reset_email_html.html",
    "emails/activation_email.txt": "activation_email.html",
    "emails/email_change.txt": "email_change.html",
    "emails/confirm_email_change.txt": "confirm_email_change.html",
    "emails/enroll_email_allowedmessage.txt": "enroll_email_allowedmessage.html",
    "emails/enroll_email_enrolledmessage.txt": "enroll_email_enrolledmessage.html",
    "emails/unenroll_email_allowedmessage.txt": "unenroll_email_allowedmessage.html",
    "emails/unenroll_email_enrolledmessage.txt": "unenroll_email_enrolledmessage.html",
}
