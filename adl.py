Components = {
    'ServerRequestHandler': 'ServerRequestHandler',
    'Invoker': 'Invoker',
    'AMoTBroker': 'AMoTBroker',

    'AMoTClient': 'AMoTClient',
    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Invoker',
    'Invoker': 'AMoTBroker',

    'AMoTClient': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler',

    'AMoTSubscriber': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

Roles = {
    # 'publisher',
    'subscriber'
}

SubscriberConfigs = {
    'timeout': 5000,
    'topics': ['Hello'],
    'host': '192.168.0.102',
    'port': 60001,
    'component': 'AMoTSubscriber'
}

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000,
}

Starter = {
    # 'AMoTPublisher', 'ServerRequestHandler'
    'AMoTClient'
}

Adaptability = {
    'Type': None
}

# ADL used in the AMoT Broker
# Components = {
#     'ServerRequestHandler': 'ServerRequestHandler',
#     'Invoker': 'Invoker',
#     'AMoTBroker': 'AMoTBroker'
# }
#
# Attachments = {
#     'ServerRequestHandler': 'Invoker',
#     'Invoker': 'AMoTBroker'
# }
#
# Starter = {
#     'ServerRequestHandler'
# }
#
# Adaptability = {
#     'Type': None
# }
