from threading import Thread
from EvolutiveMonitor import EvolutiveMonitor
import os
import time


class Monitor():

    def __init__(self):
        super().__init__()

    def run(self):
        evolutive_monitor = Thread(target=self.evolutive_monitoring)
        evolutive_monitor.start()

    def evolutive_monitoring(self):
        evolutive_monitor = EvolutiveMonitor()
        evolutive_monitor.run()

    def reactive_monitoring(self):
        pass

    def proactive_monitoring(self):
        pass



