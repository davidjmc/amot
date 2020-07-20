from SubscriptionManager import SubscriptionManager

class NotificationConsumer():
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self, topic, message, storage):
        subscribers = storage.filter_subscribers(topic)
        confirmed = []
        for subscriber in subscribers:
            if self.engine.attached(self).run(topic, message, subscriber) is not False:
                confirmed.append(subscriber)
        return confirmed

