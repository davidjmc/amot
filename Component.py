class Component:
    def __init__(self):
        self.engine = None

    def run(self, *args):
        pass

    def external(self):
        return self.engine.attached(self)

    def publish(self, topic, message):
        self.external().run(b'Publish', topic, message)

    def subscribe(self, topic):
        self.external().run(b'Subscribe', topic)

    def notify(self, topic, message, ip, port):
        return self.external().run(b'Notify', topic, message, ip, port)

    def adapt(self, adaptability, message, ip, port):
        return self.external().run(adaptability, message, ip, port)