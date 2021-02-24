from datetime import datetime
import time
import http.client

class App():
    def __init__(self):
        super().__init__()
        self.count = 0


    def subscribe(self):
        for topic in AmotEngine._app_vars['topics']:
            AmotEngine.subscribe(self, topic)


    def run(self, topic, message):
        print(':::T1:::', datetime.now().timestamp())
        print('Recebido: "{0}" em "{1}"'.format(message, topic))
        conn = http.client.HTTPConnection('localhost:5000')
        print(str(message).split(' ')[2])
        conn.request('GET', '/waterlevel?thing_id=10&water_level={0}'.format(str(message).split(' ')[2]))
        pass
