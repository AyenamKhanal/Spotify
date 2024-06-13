
from functools import wraps
from flask import session, redirect
from datetime import datetime


def access_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("access_token") is None:
            return redirect('/login')
        return f(*args, **kwargs)
    
    return decorated_function

def session_expiry(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if datetime.now().timestamp() > session['expires_at']:
            return redirect('/refresh-token')
        return f(*args, **kwargs)
    
    return decorated_function

def generate_headers():
    return  {'Authorization': f"Bearer {session['access_token']}"}
