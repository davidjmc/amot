
class AdaptationProxy():

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self, adaptability, message, ip, port):
        message = {
            'op': b'Adapt',
            'topic': adaptability,
            'msg': message
        }

        return self.engine.attached(self).run(message, ip, port)
