from AMoTEngine import Component

topic_pub = 'Hello'

class AMoTClient(Component):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.sensor = dht.DHT11(machine.Pin(2))

    def run(self):

        # Test publisher application running on the Computer
        msg = 'Hello #%d' % self.count
        self.publish(topic_pub, msg)
        self.count += 1

        # Test publisher application running on the device (thing)
        temp, hum = self.read_sensor()
        msg = 'Temperature: {} and Humidity: {}'.format(temp, hum)
        self.publish(topic, msg)

    def read_sensor(self):
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()
            hum = self.sensor.humidity()
            if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
                temp = (b'{0:3.1f},'.format(temp))
                hum = (b'{0:3.1f},'.format(hum))
                return temp, hum
            else:
                return 'Invalid sensor readings.'
        except OSError as e:
            return 'Failed to read sensor.'
