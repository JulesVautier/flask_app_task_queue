import sys

from app.services.email_service import EmailService
from app.services.service_types import ServiceTypes
from app.services.services import Service
from app.services.slack_service import SlackService


def task_handler(args):
    service_type = args['service_type']
    message = args['message']
    for service_class in Service.__subclasses__():
        if service_class().service_type == service_type:
            service_class().send_data(message)
    return True