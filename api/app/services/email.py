from flask import Flask

from .service_types import ServiceTypes
from .services import Service

from flask_mail import Mail, Message
import os

app_flask = Flask(__name__)



app_flask.config.update(mail_settings)
mail = Mail(app_flask)

class EmailService(Service):
    service_type = ServiceTypes.EMAIL

    def send_data(self, data):
        print('send email', data)