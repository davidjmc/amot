Components = {
    'AMoTClient': 'AMoTClient',
    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'AMoTClient': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

Functions = {
    # 'publisher',
    'subscriber'
}

SubscriberTopics = {
    'hello'
}

SubscriberTimeLimit = 5000

Configs = {
    'serverIP': '192.168.0.102',
    'serverPort': 60000,
    'listenPort': 60001,
}

Starter = {
    #'AMoTPublisher', 'ServerRequestHandler'
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
