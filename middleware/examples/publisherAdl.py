Components = {
    'Client': 'Client',
    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'Client': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler',
    'AdaptationAgent': 'ClientProxy'
}


SubscriberConfigs = { }

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000
}

Starter = {
    'Client'
}

Adaptability = {
    'kind': b'Evolutive'
}
