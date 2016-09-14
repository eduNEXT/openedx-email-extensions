# -*- coding: utf-8 -*-
"""
Utility functions to be used in the edx-platform codebase.
"""
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.template import loader

from openedx_email_extensions import settings
from edxmako import add_lookup, LOOKUP



def get_html_message(context, template=None, base=None):
    """
    """
    if not settings.ENABLE_MULTIPART_EMAIL:
        return None

    if base:
        html_template = settings.COMPATIBILITY.get(base, None)

        if not html_template:
            # TODO: log this properly
            print "************************** warn *****************************"
            print "we do not have a compatible template for {}".format(base)
            print "************************ end warn ***************************"

            return None  # Not really the best, we should leave that to the render_to_string, in case the theme or someone else does have the template
    else:
        html_template = template

    return loader.render_to_string(html_template, context)
    # TODO: catch possible errors of not having one of the templates
    #       log that somewhere and return None so that send mail ignores the kwarg
