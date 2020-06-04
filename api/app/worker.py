import sys

from app.services.email_service import EmailService
from app.services.slack_service import SlackService


def task_handler(args):
    # EmailService().send_data(args)
    SlackService().send_data(args)
    # this function takes around 2 minutes to complete
    print('test {}'.format(args), file=sys.stderr)
    return True