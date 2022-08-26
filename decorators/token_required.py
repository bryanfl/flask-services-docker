from functools import wraps
from flask import request, jsonify
from flask.wrappers import Response
import jwt
import datetime

secret_key = 'secret_key_bmfl'

def get_time_exp(hour):
    time_exp = datetime.datetime.utcnow() + datetime.timedelta(hours=hour)
    return time_exp

def custom_401(error):
    return Response(error, 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return custom_401('a valid token is missing')

        try:
            jwt.decode(token, secret_key, algorithms='HS256')
        except Exception as ex:
            print(ex)
            return custom_401('token is invalid')

        return f(*args, **kwargs)
    return decorator