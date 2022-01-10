adl = {
    'components': {
        'BrokerProxy': 'NewBrokerProxy', 'Marshaller': 'NewMarshaller', 'ServerRequestHandler': 'NewServerRequestHandler', 'BrokerEngine': 'NewBrokerEngine'
    },
    'attachments': {
        'BrokerProxy':'ServerRequestHandler','ServerRequestHandler':'Marshaller','Marshaller':'BrokerEngine'
    },
    'configuration': {
        'start': 'BrokerProxy',
        'ataptability': {
            'type': 'None',
            'timeout': None
        },
        'otherConfigs': {}
    }
}