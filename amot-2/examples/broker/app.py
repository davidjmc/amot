from AMoTEngine import Amot

class App:
  def __init__(self):
    super().__init__()

  def setup(self):
    # Amot.proxy().listenPublishers() # thread 2
    # Amot.proxy().listenSubscribers() # thread 3
    Amot.proxy().listen() # thread separada
    pass

  def loop(self):
    pass