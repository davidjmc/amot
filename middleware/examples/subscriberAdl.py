Components = {
    'App': 'App',
    'Subscriptor': 'Subscriptor',
    'ServerRequestHandler': 'ServerRequestHandler',
    'Notifier': 'Notifier',

    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    'ClientRequestHandler': 'ClientRequestHandler',

    'AdaptationProxy': 'AdaptationProxy'
}

Attachments = {
    'ServerRequestHandler': 'Unmarshaller',
    'Unmarshaller': 'Notifier',
    'Notifier': 'App',

    # 'Subscriptor': 'QueueProxy',
    'App': 'QueueProxy',
    'QueueProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler',

    'Executor': 'AdaptationProxy',
    'AdaptationProxy': 'Marshaller'
}


Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    'kind': None
}
