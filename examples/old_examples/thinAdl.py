Components = {
    'App': 'TemperatureChecker',
    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'App': 'QueueProxy',
    'QueueProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler'
}


Starter = {
    'App'
}

Adaptability = {
    # 'kind': b'Evolutive'
    'kind': None
}
