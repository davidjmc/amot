Component = {
    'subscriber'
}

Publisher = {}

Subscriber = {
    'timeout': None,
    'topics': [b'temperature'],
    'host': b'192.168.0.102',
    'port': b'60001'
}

# AMoT-Server IP Address and Port
Server = {
    'host': b'192.168.0.102',
    'port': 60000
}

Adaptation = {
    'host': b'192.168.0.102',
    'port': 60010,
    'timeout': 10
}
