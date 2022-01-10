from AMoTAgent import AmotAgent

_env = {}
with open('env.ini', 'r') as f:
  for line in f:
    if line.strip() == '':
      continue
    [key, val] = [p.strip() for p in line.split('=')]
    _env[key] = val

# _env['THING_ID'] = # get from thing
AmotAgent._env = _env
AmotAgent.thingStart()

import socket
ip = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0]
except:
    ip = '127.0.0.1'
finally:
    s.close()

from AMoTEngine import AmotEngine
from app import App

AmotEngine.setInstanceWith(ip, _env)
AmotEngine.getInstance().run(App())
# try:
# except:
#     print("erro na engine")
#     try:
#         machine.reset()
#     except NameError:
#         print("cant reset")
#         pass
