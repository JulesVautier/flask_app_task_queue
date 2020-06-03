from app.app.services.service_types import ServiceTypes
from app.app.services.services import Service

class LogService(Service):
    service_type = ServiceTypes.LOG

    def send_data(self, data):
        print('send log', data)