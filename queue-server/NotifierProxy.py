
class NotifierProxy():

    def __init__(self):
        super().__init__()

    def run(self, topic, message, address):
        message = {
            'op': b'Notify',
            'topic': topic,
            'msg': message
        }
        (ip, port) = address

        return AmotEngine.attached(self).run(message, ip, port)
