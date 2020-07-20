from Component import Component


class Notifier(Component):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine


    def run(self, *args):
        message = args[0]
        self.external().run(message['topic'], message['msg'])
        pass
