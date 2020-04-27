from AMoTEngine import Component

topic_pub = 'Hello'

class AMoTClient(Component):
    def __init__(self):
        super().__init__()
        self.count = 0

    def run(self):
        msg = 'Hello #%d' % self.count
        self.publish(topic_pub, msg)
        self.count += 1
