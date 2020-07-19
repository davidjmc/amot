from Component import Component


class Requestor(Component):

    def __init__(self):
        super().__init__()
        self.pkg = None

    def run(self, *args):
        request = args[0]

        self.pkg = request.op
        self.pkg += b' ' + request.topic
        self.pkg += b' ' + request.message

        package = {
            'Destination': args[1],
            'DPort': args[2],
            'Payload': self.pkg
        }

        return self.external().run(package)
