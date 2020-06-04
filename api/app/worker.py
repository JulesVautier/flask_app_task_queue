from app.services.services import Service


def task_handler(args):
    service_type = args['service_type']
    message = args['message']
    for service_class in Service.__subclasses__():
        if service_class().service_type == service_type:
            service_class().send_data(message)
    return True