def created(created_id=None):
    response = {
        'code' : 201,
        'status' : 'Created',
        'message' : 'A resource has been created or updated successfully'
    }
    if created_id:
        response['id'] = created_id
    return response


def bad_request(fields):
    return {
        'code' : 400,
        'status' : 'Bad Request',
        'message' : 'The request cannot be fulfilled due to bad syntax or an invalid parameter',
        'Fields' : fields
    }


def deleted():
    return {
        'code' : 204,
        'status' : 'No Content',
        'message' : 'The server has successfully fulfilled the request and there is no aditional content to send in the response payload body'
    }