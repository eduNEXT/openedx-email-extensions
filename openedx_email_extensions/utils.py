# -*- coding: utf-8 -*-
"""
Utility functions to be used in the edx-platform codebase.
"""
from __future__ import absolute_import, unicode_literals

import logging
from django.conf import settings
from django.template import loader, TemplateDoesNotExist

from openedx_email_extensions import settings
from edxmako import add_lookup, LOOKUP

log = logging.getLogger(__name__)


def get_html_message(context, template=None, base=None):
    """
    """
    if not settings.ENABLE_MULTIPART_EMAIL:
        return None

    if base:
        html_template = settings.COMPATIBILITY.get(base, None)

        if not html_template:
            log.warning("We do not have a compatible template for {}".format(base))
    else:
        html_template = template

    try:
        return loader.render_to_string(html_template, context)
    except TemplateDoesNotExist:
        log.warning("We tried to render an unexistant template for {}".format(html_template))
        return None
