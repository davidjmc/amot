Components = {
    'ServerRequestHandler': 'ServerRequestHandler',
    'NotifierProxy': 'NotifierProxy',
    'NotificationEngine': 'NotificationEngine',
    'NotificationConsumer': 'NotificationConsumer',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Unmarshaller',
    'Unmarshaller': 'NotificationEngine',
    'NotificationEngine': 'NotificationConsumer',
    'NotificationConsumer': 'NotifierProxy',
    'NotifierProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler'

    # 'ServerRequestHandler->Marshaller->QueueServer',
    # 'QueueServer->ClientProxy->Marshaller->ClientRequestHandler'
}

Roles = {
    'server'
}

SubscriberConfigs = { }

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000,
}

Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    'kind': None
}
