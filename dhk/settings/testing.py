from .base import *

import logging

class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


ENVIRONMENT = 'testing'

MIGRATION_MODULES = DisableMigrations()

LOG_RESPONSE_TIMES = False

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# disable all loggers
LOGGING['loggers']['ikagei']['level'] = 'CRITICAL'
logging.disable(logging.CRITICAL)
