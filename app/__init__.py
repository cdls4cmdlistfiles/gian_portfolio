
from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ak$%^(bajsd)'
       # mail config
    
    app.config["MAIL_SERVER"] = "smtp.gmail.com"  # SMTP Server
    app.config["MAIL_PORT"] = 587  # Port for TLS
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False
    app.config["MAIL_USERNAME"] = "gianerminoespineda@gmail.com"  # Your email
    app.config["MAIL_PASSWORD"] = "ysyrldenznyrgcll"  # App password or actual password
    app.config["MAIL_DEFAULT_SENDER"] = "roleplay@gmail.com"

    from app.views import app as views
    app.register_blueprint(views)
    mail.init_app(app)

    return app




