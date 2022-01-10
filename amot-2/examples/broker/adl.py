adl = {
    'components': {
        # ClassName: FileName
        'BrokerProxy': 'BrokerProxy',
        'Marshaller': 'Marshaller',
        'ClientRequestHandler': 'ClientRequestHandler'
    },
    'attachments': {
        'BrokerProxy':'ServerRequestHandler',
        'ServerRequestHandler': 'Marshaller',
        'Marshaller':'BrokerEngine'
    },
    'configuration': {
        'start': 'BrokerProxy',
        'adaptability': {},
        'scalability': {}
    }
}