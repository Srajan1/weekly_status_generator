from django.http import JsonResponse

FAILURE = 'fail'
SUCCESS = 'success'

def error_response(error_code, message, data=None):
    response = {}
    response['status'] = FAILURE
    response['error_code'] = error_code
    response['message'] = message
    if data:
        response['data'] = data
    return JsonResponse(response)

def success_response(status_code, message, data=None):
    response = {}
    response['status'] = SUCCESS
    response['status_code'] = status_code
    response['message'] = message
    if data:
        response['data'] = data
    return JsonResponse(response)