from AMoTEngine import Amot
import time

class App:
  def __init__(self):
    super().__init__()

  def setup(self):
    # start listen
    pass

  def loop(self):
    print('listen')
    Amot.proxy().listen() # thread separada
    # do something
    print('let me sleep')
    time.sleep(5)
    pass