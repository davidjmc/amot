class NotificationEngine(Component):

    # topics where messages are posted
    topics = {}

    def __init__(self):
        super().__init__()

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
        elif operation == b'Unsubscribe':
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