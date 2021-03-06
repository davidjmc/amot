from datetime import datetime
import time

class App():
    def __init__(self):
        super().__init__()
        self.count = 0


    def subscribe(self):
        for topic in AmotEngine.subscriber_configs['topics']:
            AmotEngine.subscribe(self, topic)


    def run(self, topic, message):
        AmotEngine._times.append(('--app0', time.time()))
        print(':::T1:::', datetime.now().timestamp())
        print('Recebido: "{0}" em "{1}"'.format(message, topic))
        AmotEngine._times.append(('--app1', time.time()))
        # print(datetime.now(), package.topic, package.message)
        pass
