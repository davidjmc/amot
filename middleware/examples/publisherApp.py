import time
import random as r

from Component import Component
from datetime import datetime

topic = b'temperature'


class Client(Component):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.count = 0
        # self.sensor = dht.DHT11(machine.Pin(2))

    def run(self):

        # Test publisher application running on the Computer
        temp, hum = self.temp_hum_sensor()
        msg = b'Temperature: %b and Humidity: %b' % (temp, hum)
        print(self.count, msg)
        print(':::T0:::', datetime.now().timestamp())
        self.publish(topic, msg)
        self.count += 1
        time.sleep(1)

        # Test publisher application running on the device (thing)
        # temp, hum = self.read_sensor()
        # msg = 'Temperature: {} and Humidity: {}'.format(temp, hum)
        # self.publish(topic, msg)

    @staticmethod
    def temp_hum_sensor():
        try:
            temp = 30.0 * r.random()
            hum = 30.0 * r.random()
            if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
                temp = b'%3.1f' % temp
                hum = b'%.1f' % hum
                return temp, hum
            else:
                return 'Invalid sensor reading'
        except OSError as e:
            return 'Failed to read sensor.'

# def read_sensor(self):
#         try:
#             self.sensor.measure()
#             temp = self.sensor.temperature()
#             hum = self.sensor.humidity()
#             if (isinstance(temp, float) and isinstance(hum, float)) or
#             (isinstance(temp, int) and isinstance(hum, int)):
#                 temp = (b'{0:3.1f},'.format(temp))
#                 hum = (b'{0:3.1f},'.format(hum))
#                 return temp, hum
#             else:
#                 return 'Invalid sensor readings.'
#         except OSError as e:
#             return 'Failed to read sensor.'









