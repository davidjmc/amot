from Component import Component

class AdaptationProxy(Component):

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self, adaptability, message, ip, port):
        message = {
            'op': b'Adapt',
            'topic': adaptability,
            'msg': message
        }

        return self.external().run(message, ip, port)
