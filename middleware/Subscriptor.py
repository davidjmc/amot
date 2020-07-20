from Component import Component

class Subscriptor(Component):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.subscribe(topic)