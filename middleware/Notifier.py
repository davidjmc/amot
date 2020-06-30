from AMoTEngine import Component, Message


class Notifier(Component):
    def __init__(self):
        super().__init__()


    def run(self, *args):
        message = args[0]
        self.external().run(message.topic, message.message)
        pass
