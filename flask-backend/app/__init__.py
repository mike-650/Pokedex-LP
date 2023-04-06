import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect, generate_csrf # import statement for CSRF
from ..config import Configuration
# from ..routes import 

app = Flask(__name__)

app.config.from_object(Configuration)

app.register_blueprint()

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
