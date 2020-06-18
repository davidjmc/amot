from AMoTEngine import Component

class Invoker(Component):
    def _init_(self):
        super()._init_()

    def run(self, *args):
        package = args[0]
        request = None
        if package is None:
            return

        if b'Publish' in package:
            invocation = package.split(b' ', 2)
            request = self.Request(invocation[0], invocation[1], invocation[2])
        elif b'Subscribe' in package:
            invocation = package.split(b' ', 2)
            request = self.Request(invocation[0], invocation[1], invocation[2])
        elif b'Notify' in package:
            invocation = package.split(b' ', 2)
            request = self.Request(invocation[0], invocation[1], invocation[2])
        elif b'Adapt' in package:
            invocation = package.split(b' ', 2)
            request = self.Request(invocation[0], invocation[1], invocation[2])
        else:
            print('Notification engine :: Operation is not implemented by AMoT Engine')

        return self.external().run(request)