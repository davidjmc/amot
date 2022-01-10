from AMoTEngine import Amot
from time import sleep

class App:
  def __init__(self):
    super().__init__()

  def setup(self):
    Amot.proxy().subscribe('temp')
    pass

  def loop(self):
    msg = Amot.proxy().checkMsg()
    if msg:
      print(msg)
    sleep(1)
    pass