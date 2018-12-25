"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.exceptions import ImproperlyConfigured

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dhk.settings.local")

application = get_wsgi_application()
