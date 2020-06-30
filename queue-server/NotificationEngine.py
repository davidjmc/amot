from AMoTEngine import Component, Message
from SubscriptionManager import SubscriptionManager
from collections import deque

class NotificationEngine(Component):

    # topics where messages are posted

    def __init__(self):
        super().__init__()
        self.storage = SubscriptionManager()

    def run(self, *args):
        message = args[0]
        operation = message.op
        topic = message.topic
        message = message.message

        if operation == b'Publish':
            subscribers_notified = self.external().run(topic, message, self.storage)
            self.storage.keep_subscribers(topic, subscribers_notified)
        elif operation == b'Subscribe':
            ip_port = message.split(b' ')
            self.subscribe(topic, ip_port[0], int(ip_port[1]))
        elif operation == b'Unsubscribe':
            # TODO
            pass
        else:
            print(
                'Notification engine :: Operation ' +
                str(args[0]['Operation']) +
                'is not implemented by AMoT Engine'
            )

    def publish(self, topic, message):
        ret = False
        if topic in self.topics.keys():
            self.topics[topic].append(message)
            if self.topics[topic].__contains__(message):
                ret = True
        else:
            self.topics[topic] = deque([message], maxlen=20)
            if self.topics[topic].__contains__(message):
                ret = True
        return ret

    def subscribe(self, topic, ip, port):
        subscriber_address = (ip, port)
        self.storage.add_subscriber(topic, subscriber_address)