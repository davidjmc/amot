import pickle
import socket
from collections import deque

from AMoTEngine import Component, Message


class QueueServer(Component):
    # topics where messages are posted
    topics = {}

    # AMoT-Clients list subscribed to some topic
    subscribers = {}

    def __init__(self):
        super().__init__()
        self.subscriber_manager = SubscriberManager()
        self.notify_consumer = NotificationConsumer()

    def run(self, *args):
        message = args[0]
        operation = message.op
        topic = message.topic
        message = message.message

        if operation == b'Publish':
            self.publish(topic, message)
            self.notify_subscribers(topic)
        elif operation == b'Subscribe':
            ip_port = message.split(b' ')
            self.subscriber(topic, ip_port[0], int(ip_port[1]))
        elif operation == b'Adapt':
            invocation = {'Operation': args[0], 'Topic': args[1]}
            self.external().run(invocation)
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

    def subscriber(self, topic, ip, port):
        subscriber_address = (ip, port)
        self.subscribers = self.subscriber_manager.add_subscriber(self.subscribers, topic, subscriber_address)

    # Notify the subscribers by topics
    def notify_subscribers(self, topic):
        subscribers = self.subscriber_manager.filter_subscribers(self.subscribers, topic)

        if subscribers is not None:
            if self.topics[topic] is not None:
                non_notification = self.notify_consumer.notify_subscriber(
                    subscribers, topic, self.topics[topic][-1], self
                )
                self.subscribers = self.subscriber_manager.remove_subscriber(
                    self.subscribers, topic, non_notification
                )
                self.topics[topic].pop()


class SubscriberManager:

    @staticmethod
    def add_subscriber(subscribers, topic, address):
        if topic in subscribers.keys():
            if address not in subscribers[topic]:
                subscribers[topic].append(address)
        else:
            subscribers[topic] = deque([address], maxlen=20)
        return subscribers

    @staticmethod
    def remove_subscriber(subscribers, topic, subs):
        if topic in subscribers.keys():
            for subscriber in subs:
                if subscriber in subscribers[topic]:
                    subscribers[topic].remove(subscriber)
        return subscribers

    @staticmethod
    def filter_subscribers(subscribers, topic):
        subs = None
        if topic in subscribers.keys():
            subs = subscribers[topic]
        return subs


class NotificationConsumer:

    @staticmethod
    def notify_subscriber(subscribers, topic, message, pog):
        non_subscribers_notification = []
        for subscriber in subscribers:
            sent = pog.notify(topic, message, subscriber[0], subscriber[1])
            if not sent:
                print('Error when sending data on the NotificationConsumer')
                non_subscribers_notification.append(subscriber)
            # try:
            # except OSError as e:
            # sock = socket.socket()
            # try:
            #     sock.connect(subscriber)
            #     data = pickle.dumps(message)
            #     sent = sock.sendall(data)
            #     print(sent)
            #     sock.close()
            # except OSError as e:
            #     print('Error when sending data on the NotificationConsumer: ', e)
            #     non_subscribers_notification.append(subscriber)
        return non_subscribers_notification