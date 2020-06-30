from AMoTEngine import Component
from SubscriptionManager import SubscriptionManager

class NotificationConsumer(Component):
    def __init__(self):
        super().__init__()

    def run(self, topic, message, storage):
        subscribers = storage.filter_subscribers(topic)
        confirmed = []
        for subscriber in subscribers:
            if self.external().run(topic, message, subscriber) is not False:
                confirmed.append(subscriber)
        return confirmed

