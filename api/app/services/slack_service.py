from app.services.service_types import ServiceTypes
import os

from app.services.services import Service
from slack import WebClient

client = WebClient(token=os.environ['SLACK_API_TOKEN'])

class SlackService(Service):
    service_type = ServiceTypes.SLACK

    def send_data(self, message):
        response = client.chat_postMessage(
            channel='#notifs-plateforme',
            text=message)
