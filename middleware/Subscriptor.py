from Component import Component

class Subscriptor(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.subscribe(topic)