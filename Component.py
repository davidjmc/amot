class Component:
    def __init__(self):
        self.engine = None

    def run(self, *args):
        pass

    def publish(self, topic, message):
        self.engine.attached(self).run(b'Publish', topic, message)

    def subscribe(self, topic):
        self.engine.attached(self).run(b'Subscribe', topic)

    def notify(self, topic, message, ip, port):
        return self.engine.attached(self).run(b'Notify', topic, message, ip, port)

    def adapt(self, adaptability, message, ip, port):
        return self.engine.attached(self).run(adaptability, message, ip, port)