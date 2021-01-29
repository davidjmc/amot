thing = {
    'id': '2',
    'location': None,
    'listen_port': 60001
}

broker = {
    'host': '192.168.0.102',
    'port': 60000,
}

server = {
    'host': '192.168.0.102',
    'port': 60010,
    'type': None, # or evolutive or reactive or proactive ## unecessary
    'timeout': None # adaptation interval ## unecessary
}

app_vars = {
    'mode': 'subscriber', # or subscriber or sublish_subscriber or broker
    'topics': [b'temperature', b'temp'] # and/or other topics
}






# Component = {
#     'subscriber'
# }

# Publisher = {}

# Subscriber = {
#     'timeout': None,
#     'topics': [b'temperature', b'temp'],
#     'host': b'192.168.0.102',
#     'port': b'60001'
# }

# # AMoT-Server IP Address and Port
# Server = {
#     'host': b'192.168.0.102',
#     'port': 60000
# }

# Adaptation = {
#     'host': b'192.168.0.102',
#     'port': 60010,
#     'timeout': 10
# }
