#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
from mako.template import Template
from mako.lookup import TemplateLookup
from django.core.management.base import BaseCommand
from django.template import loader, TemplateDoesNotExist

from openedx_email_extensions import settings

# Patches to the modules that would be in openedx
import mock


def _fake_everything():
    """
    This function fills the gaps so that mako thinks we are running in a real environment
    """
    def fake_get_value(value, default):
        return default

    def fake_get_template_path(value):
        return value

    fake_microsite = mock.Mock()
    fake_microsite.microsite.get_value = fake_get_value
    fake_microsite.microsite.get_template_path = fake_get_template_path

    sys.modules["microsite_configuration"] = fake_microsite
    sys.modules["openedx.core.djangoapps.site_configuration"] = fake_microsite
    sys.modules["openedx.core.djangoapps"] = mock.Mock()
    sys.modules["openedx.core"] = mock.Mock()
    sys.modules["openedx.conf"] = mock.Mock()
    sys.modules["openedx"] = mock.Mock()
    sys.modules["django.core.urlresolvers"] = mock.Mock()


class Command(BaseCommand):
    """
    Command to render all the templates
    """

    def handle(self, *args, **options):
        """
        Render all the known templates with a test context
        """
        _fake_everything()

        mylookup = TemplateLookup(
            directories=[settings.TEMPLATES_PATH],
            output_encoding='utf-8',
            input_encoding='utf-8',
            default_filters=['decode.utf8'],
            encoding_errors='replace',
        )

        context = {
          "site": "{site}",
          "site_name": "{site_name}",
          "course_url": "{course_url}",
          "course_about_url": "{course_about_url}",
          "full_name": "{full_name}",
          "email_address": "{email_address}",
          "old_email": "{old_email}",
          "new_email": "{new_email}",
          "uid": "{uid}",
          "token": "{token}",
          "protocol": "{protocol}",
          "site": "{site}",
          "key": "{key}",
          "course": mock.Mock(),
          "settings": mock.Mock(),
          "is_shib_course": False,
          "auto_enroll": False,
          "registration_url": "{registration_url}",
        }

        for base_name, name in settings.COMPATIBILITY.iteritems():
            content = mylookup.get_template(name).render(**context)

            filename = settings.REPO_ROOT / "rendered" / name
            # Create the dir if does not exists
            try:
                os.makedirs(filename.dirname())
            except OSError:
                if not os.path.isdir(filename.dirname()):
                    raise

            with open(filename, 'w') as my_file:
                print(content, file=my_file)
