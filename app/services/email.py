from app.services.service_types import ServiceTypes
from app.services.services import Service

class EmailService(Service):
    service_type = ServiceTypes.EMAIL

    def send_data(self, data):
        print('send email', data)