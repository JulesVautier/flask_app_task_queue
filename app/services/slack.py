from app.services.service_types import ServiceTypes
from app.services.services import Service

class SlackService(Service):
    service_type = ServiceTypes.SLACK

    def send_data(self, data):
        print('send email', data)