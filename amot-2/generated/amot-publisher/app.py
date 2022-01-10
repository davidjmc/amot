from AMoTEngine import Amot
import time
import random as r

class App:
  def __init__(self):
    super().__init__()
    self.count = 0

  def setup(self):
    print('setting things up')
    pass

  def loop(self):
    topics = Amot.config('topics')

    temp, hum = self.temp_hum_sensor()
    # msg = 'Temperature: %s and Humidity: %s @ %s' % (temp, hum, 'lalala')
    msg = [temp, hum, ['test', 'oi,virgula']]

    self.count += 1

    print('Publishing on topic [{0}]: {1}'.format(topics, msg))

    Amot.proxy().publish(topics, msg)

    time.sleep(Amot.config('interval'))

  def temp_hum_sensor(self):
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