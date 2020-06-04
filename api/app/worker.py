import sys

from app.services.email import EmailService


def task_handler(args):
    EmailService().send_data(args)
    # this function takes around 2 minutes to complete
    print('test {}'.format(args), file=sys.stderr)
    return True