thing = {
    'id': '11',
    'location': None
}

broker = {
    'host': b'192.168.0.102',
    'port': b'60000'
}

server = {
    'host': b'192.168.0.102',
    'port': b'60010',
    'type': None, # or evolutive or reactive or proactive ## unecessary
    'timeout': None # adaptation interval ## unecessary
}

app_vars = {
    'mode': 'publisher', # or subscriber or sublish_subscriber or broker
    'topics': [b'temp'] # and/or other topics
}