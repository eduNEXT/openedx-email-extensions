# -*- coding: utf-8 -*-
"""
This is the settings file for the openedx_email_extensions application
"""

from path import Path as path

try:
    from openedx.conf import settings
except ImportError:
    # Fall back to regular settings if there isn't a site aware settings module
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

DEFAULT_EXTRA_FOOTER_TEMPLATE = None

DEFAULT_EMAIL_COLORS = {
  "email_wrapper__background": "#F3F3F3",
  "email_body__color": "#0A0A0A",
  "email_body__background": "#FEFEFE",
  "email_button__color": "#FEFEFE",
  "email_button__background": "#2DAAE1",
  "email_button__border": "#2DAAE1",
  "email_footer__color": "#0A0A0A",
  "email_footer__color_link": "#2DAAE1",
  "email_footer__color_small": "#B1B1B1"
}

class ProxySettings(object):
    """
    This object is a proxy for the django.conf settings object. It defaults to a 
    local variable of this module prefixed with DEFAULT_
    """

    def __getattr__(self, name):
        try:
            return getattr(settings, name)
        except AttributeError:
            default_name = "DEFAULT_{}".format(name)
            return globals().get(default_name)


proxy_settings = ProxySettings()
