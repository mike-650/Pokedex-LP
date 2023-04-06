import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect, generate_csrf # import statement for CSRF
from .config import Configuration
from .models import db
from flask_migrate import Migrate
# from ..routes import 

app = Flask(__name__)

app.config.from_object(Configuration)

# app.register_blueprint()

db.init_app(app)

Migrate(app,db)






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





#flask db init 
#flask db migrate
#flask db upgrade