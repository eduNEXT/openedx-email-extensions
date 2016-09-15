# -*- coding: utf-8 -*-
"""
openedx_email_extensions Django application initialization.
"""

from openedx_email_extensions import settings
from edxmako import add_lookup, clear_lookups


def run():
    """
    Setup mako lookup directories.
    IMPORTANT: This method can be called multiple times during application startup. Any changes to this method
    must be safe for multiple callers during startup phase.
    """
    # This is not idempotent yet, but the run() method in edxmako clears it, so we are safe for now
    # TODO: make this safe without the need for edxmako
    add_lookup('main', settings.TEMPLATES_PATH)
