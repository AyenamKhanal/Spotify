
from functools import wraps
from flask import session, redirect, render_template
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


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def getkey(num):

    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]

    return keys[int(num)]