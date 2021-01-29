thing = {
    'id': '1',
    'location': None
}

broker = {
    'host': '192.168.0.102',
    'port': 60000
}

server = {
    'host': '192.168.0.102',
    'port': 60010,
    'type': None, # or evolutive or reactive or proactive ## unecessary
    'timeout': None # adaptation interval ## unecessary
}

app_vars = {
    'mode': 'publisher', # or subscriber or sublish_subscriber or broker
    'topics': [b'temperature'] # and/or other topics
}