class AdaptationProxy(Component):
    def __init__(self):
        super().__init__()


    def run(self):
        return self.external().run(message, ip, port)
