import network
import ubinascii
import gc
import time

# set the local area network configuration
SSID='MULTILASER 1200AC 2.4G'
PASSWORD='123456789'

thing = network.WLAN(network.STA_IF)
if not thing.isconnected():
  print('Connecting to local area network...')
  thing.active(True)
  thing.connect(SSID, PASSWORD)
while not thing.isconnected():
  pass
print('Connection sucessful')
print(thing.ifconfig())


# get the thing network IP 
thing_ip = thing.ifconfig()[0]


# get the thing unique ID
thing_id = str(ubinascii.hexlify(machine.unique_id()), 'ascii')
print(thing_id)

gc.collect()

from AMoTAgent import AmotAgent
AmotAgent.thingStart(thing_id)

gc.collect()

from AMoTEngine import AmotEngine
AmotEngine(thing_ip).run()
