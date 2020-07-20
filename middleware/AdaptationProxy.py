from Component import Component

class AdaptationProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, adaptability, message, ip, port):
        message = {
            'op': b'Adapt',
            'topic': adaptability,
            'msg': message
        }

        return self.external().run(message, ip, port)
