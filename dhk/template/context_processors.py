from django.conf import settings


def get_globals(request):
    return {
        'ENVIRONMENT': settings.ENVIRONMENT,
    }
