class Service:
    service_type = None

    def send_data(self, message):
        raise NotImplementedError

