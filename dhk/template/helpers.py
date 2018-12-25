from django.utils import timezone
from django.core.urlresolvers import reverse, NoReverseMatch
from markupsafe import Markup
import json
from utils.helpers import JSONDateTimeEncoder


def localtime(date_object):
    return timezone.localtime(date_object)


def is_current_url(request, url):
    try:
        pattern = '^%s$' % reverse(url)
    except NoReverseMatch:
        pattern = url
    return (pattern == request.path)


def jsonify(obj):
    return Markup(json.dumps(obj, cls=JSONDateTimeEncoder))
