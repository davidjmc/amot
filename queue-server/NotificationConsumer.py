from SubscriptionManager import SubscriptionManager

class NotificationConsumer():
    def __init__(self):
        super().__init__()

    def run(self, topic, message, storage):
        subscribers = storage.filter_subscribers(topic)
        confirmed = []
        for subscriber in subscribers:
            if AmotEngine.attached(self).run(topic, message, subscriber) is not False:
                confirmed.append(subscriber)
        return confirmed

