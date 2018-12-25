from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def srs_exception_handler(exc, context):
    response = exception_handler(exc,context)

    if response != None:
        response.data['code'] = response.status_code
        resolutions = {
            400: 'Bad Request',
            401 : 'Unauthorized',
            403 : 'Unauthorized',
            404: 'Not Found',
            500 : 'Internal Server Error',
        }
        response.data['status'] = resolutions.get(response.status_code)

    return response


class DoesNotExist(APIException):
    status_code = 404
    def __init__(self, detail="This item does not exist", *args, **kwargs):
        self.default_detail = {
            'message' : detail,
        }
        super().__init__(*args, **kwargs)


class PermissionDenied(APIException):
    status_code = 403
    def __init__(self, detail="You don’t have enough permissions to access this resource on the server", *args, **kwargs):
        self.default_detail = {
            'message' : detail
        }
        super().__init__(*args, **kwargs)


class BadRequest(APIException):
    status_code = 400
    def __init__(self, message="The request cannot be fullfilled due to bad syntax or an invalid parameter", fields=None, *args, **kwargs):
        self.default_detail = {
            'message' : message
        }
        if fields != None:
            self.default_detail['Fields'] = fields
        super().__init__(*args, **kwargs)


class DoesNotBelong(Exception):
    pass


class AlreadyExists(Exception):
    pass