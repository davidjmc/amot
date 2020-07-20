from Component import Component

class NotifierProxy(Component):

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self, topic, message, address):
        message = {
            'op': b'Notify',
            'topic': topic,
            'msg': message
        }
        (ip, port) = address

        return self.engine.attached(self).run(message, ip, port)
