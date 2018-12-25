import re
import datetime
import json
import hashlib


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(JSONDateTimeEncoder, self).default(obj)


class Hasher(object):
    def __init__(self, **kwargs):
        self.sorted_string = ''
        self.hash = self.get_hash(self.get_sorted_string(kwargs))

    def get_sorted_string(self, data):
        if isinstance(data, dict):
            for k, v in sorted(data.items()):
                string = self.get_sorted_string(v)
                self.sorted_string = "%s:%s|%s" % (k, string, self.sorted_string)
            return self.sorted_string.strip('|')
        elif isinstance(data, list):
            return '|'.join(str(x) for x in sorted(data))
        elif isinstance(data, (int, long, float)):
            return "%s" % data
        elif isinstance(data, basestring):
            return "%s" % data.replace("'", "").replace('"', '')

    def get_hash(self, string):
        identifier = hashlib.sha1()
        identifier.update(string.encode('ascii', 'ignore'))
        return identifier.hexdigest()


def convert_camel_case(txt):
    # https://stackoverflow.com/a/9283563
    # this function converts a camel cased string to space delimited
    # for e.g divLineColor -> div Line Color
    # takes into account abbreviations like SQL etc
    label = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', txt)
    return label
