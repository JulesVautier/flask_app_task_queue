from app.services.service_types import ServiceTypes
import os

from app.services.services import Service

# client = WebClient(token=os.environ['SLACK_API_TOKEN'])

class SlackService(Service):
    service_type = ServiceTypes.SLACK

    def send_data(self, data):
        response = client.chat_postMessage(
            channel='#notifs-plateforme',
            text=data)
