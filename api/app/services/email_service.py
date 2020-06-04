import os

from flask import Flask
from flask_mail import Mail, Message

from .service_types import ServiceTypes
from .services import Service

app_flask = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}
app_flask.config.update(mail_settings)
mail = Mail(app_flask)

class EmailService(Service):
    service_type = ServiceTypes.EMAIL

    def send_data(self, message):
        with app_flask.app_context():
            msg = Message(subject="Hello",
                          sender=app_flask.config.get("MAIL_USERNAME"),
                          recipients=["<recipient email here>"],  # replace with your email for testing
                          body="This is a test email I sent with Gmail and Python!")
            mail.send(msg)