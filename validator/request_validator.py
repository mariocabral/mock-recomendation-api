from functools import wraps
from flask import request, abort


def validate(function_call):
    @wraps(function_call)
    def decorated(*args, **kwargs):
        application = request.headers.get('x-application')
        platform = request.headers.get('x-platform')
        if application == 'CUS' and platform == 'AND':
            return function_call(*args, **kwargs)
        return abort(403)

    return decorated
