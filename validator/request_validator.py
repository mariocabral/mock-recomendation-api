from functools import wraps
from flask import request, abort


def validate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        application = request.headers.get('x-application')
        platform = request.headers.get('x-platform')
        if application == 'CUS' and platform == 'AND':
            return f(*args, **kwargs)
        return abort(403)

    return decorated
