thing = {
    'id': 'broker',
    'location': None,
    'listen_port': 60000
}

broker = {}

server = {
    'host': '192.168.0.102',
    'port': 60010,
    'type': None, # or evolutive or reactive or proactive ## unecessary
    'timeout': None # adaptation interval ## unecessary
}

app_vars = {
    'mode': 'broker', # or subscriber or sublish_subscriber or broker
    # 'topics': [b'temperature'] # and/or other topics
}

# Component = {
#     'server'
# }

# __id__ = 'broker'

# Publisher = {}

# Subscriber = {}

# # AMoT-Server IP Address and Port
# Server = {
#     'host': b'192.168.0.102',
#     'port': 60000
# }

# Adaptation = {
#     'host': b'192.168.0.102',
#     'port': 60010,
#     'timeout': None
# }
