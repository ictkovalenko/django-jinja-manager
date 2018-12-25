from __future__ import absolute_import  # Python 2 only
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from .helpers import localtime, is_current_url, jsonify


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'localtime': localtime,
        'is_current_url': is_current_url,
        'round': round,
        'jsonify': jsonify,
    })
    return env
