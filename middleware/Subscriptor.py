
class Subscriptor():
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.engine.attached(self).run(b'Subscribe', topic)
