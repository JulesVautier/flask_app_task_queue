import sys


def task_handler(args):
    # this function takes around 2 minutes to complete
    print('test {}'.format(args), file=sys.stderr)
    return True