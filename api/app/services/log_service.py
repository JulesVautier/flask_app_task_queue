from api.app.services.service_types import ServiceTypes
from api.app.services.services import Service

class LogService(Service):
    service_type = ServiceTypes.LOG

    def send_data(self, data):
        print('send log', data)