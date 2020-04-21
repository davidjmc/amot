import pickle
import socket
from collections import deque

from AMoTEngine import Component


class AMoTBroker(Component):
    # topics where messages are posted
    topics = {}

    # AMoT-Clients list subscribed to some topic
    subscribers = {}

    def __init__(self):
        super().__init__()

    def run(self, *args):
        invocation = args[0]
        operation = invocation['Operation']
        message = invocation['Message']

        if operation is 'Publish':
            self.publish(message['Topic'], message['Message'])
            self.notify(message['Topic'])
        elif operation is 'Subscribe':
            self.subscriber(message['Topic'], message['Source'], message['SPort'])
        elif operation is 'Adapt':
            invocation = {'Operation': args[0], 'Topic': args[1]}
            self.external().run(invocation)
        else:
            print('Notification engine :: Operation ' + args[0]['Operation'] + 'is not implemented by AMoT Engine')

    def publish(self, topic, message):
        ret = False
        if topic in self.topics.keys():
            self.topics[topic].append(message)
            if self.topics[topic].__contains__(message):
                ret = True
        else:
            self.topics[topic] = deque([message], maxlen=1)
            if self.topics[topic].__contains__(message):
                ret = True
        return ret

    def subscriber(self, topic, ip, port):
        subscriber_address = (ip, port)
        SubscriberManager().add_subscriber(self.subscribers, topic, subscriber_address)

    def notify(self, topic):
        subscribers = SubscriberManager().filter_subscribers(self.subscribers, topic)

        if subscribers is not None:
            if self.topics[topic] is not None:
                for subscriber in subscribers:
                    NotificationConsumer().notify_subscriber(subscriber, self.topics[topic][0])
                self.topics[topic].popleft()


class SubscriberManager:

    @staticmethod
    def add_subscriber(subscribers, topic, address):
        if topic in subscribers.keys():
            if subscribers[topic].__contains__(address) is None:
                subscribers[topic].append(address)
        else:
            subscribers[topic] = deque([address], maxlen=1)

        return subscribers

    def remove_subscriber(self):
        pass

    @staticmethod
    def filter_subscribers(subscribers, topic):
        subs = None
        if topic in subscribers.keys():
            subs = subscribers[topic]
        return subs


class NotificationConsumer:

    @staticmethod
    def notify_subscriber(subscriber, message):
        sock = socket.socket()
        try:
            sock.connect(subscriber)
            data = pickle.dumps(message)
            sock.sendall(data)
            sock.close()
        except OSError as e:
            print('Error when sending data on the NotificationConsumer: ', e)



