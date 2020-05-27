server:
	mkdir -p generated/amot-server
	rm -rf generated/amot-server/*
	cp middleware/examples/serverAdl.py generated/amot-server/adl.py
	cp middleware/examples/serverConfig.py generated/amot-server/config.py
	cp AMoTEngine.py generated/amot-server/
	cp pickle.py generated/amot-server/
	cp queue-server/QueueServer.py generated/amot-server/
	cp middleware/Invoker.py generated/amot-server/
	cp middleware/ServerRequestHandler.py generated/amot-server/
	cp middleware/Requestor.py generated/amot-server/
	cp middleware/ClientRequestHandler.py generated/amot-server/
	cp middleware/ClientProxy.py generated/amot-server/

publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*
	cp middleware/examples/publisherAdl.py generated/amot-publisher/adl.py
	cp middleware/examples/publisherConfig.py generated/amot-publisher/config.py
	cp AMoTEngine.py generated/amot-publisher/
	cp pickle.py generated/amot-publisher/
	cp middleware/Requestor.py generated/amot-publisher/
	cp middleware/ClientRequestHandler.py generated/amot-publisher/
	cp middleware/ClientProxy.py generated/amot-publisher/
	cp middleware/examples/publisherApp.py generated/amot-publisher/Client.py

subscriber:
	mkdir -p generated/amot-subscriber
	rm -rf generated/amot-subscriber/*
	cp middleware/examples/subscriberAdl.py generated/amot-subscriber/adl.py
	cp middleware/examples/subscriberConfig.py generated/amot-subscriber/config.py
	cp AMoTEngine.py generated/amot-subscriber/
	cp pickle.py generated/amot-subscriber/
	cp middleware/Invoker.py generated/amot-subscriber/
	cp middleware/ServerRequestHandler.py generated/amot-subscriber/
	cp middleware/Requestor.py generated/amot-subscriber/
	cp middleware/ClientRequestHandler.py generated/amot-subscriber/
	cp middleware/ClientProxy.py generated/amot-subscriber/
	cp middleware/examples/subscriberApp.py generated/amot-subscriber/App.py

publisher_subscriber:
	mkdir -p generated/amot-publisher-subscriber
	rm -rf generated/amot-publisher-subscriber/*
	cp middleware/examples/publisherSubscriberAdl.py generated/amot-publisher-subscriber/adl.py
	cp AMoTEngine.py generated/amot-publisher-subscriber/
	cp config.py generated/amot-publisher-subscriber/
	cp pickle.py generated/amot-publisher-subscriber/
	cp middleware/Invoker.py generated/amot-publisher-subscriber/
	cp middleware/ServerRequestHandler.py generated/amot-publisher-subscriber/
	cp middleware/Requestor.py generated/amot-publisher-subscriber/
	cp middleware/ClientRequestHandler.py generated/amot-publisher-subscriber/
	cp middleware/ClientProxy.py generated/amot-publisher-subscriber/
	cp middleware/examples/subscriberApp.py generated/amot-publisher-subscriber/app.py
	cp middleware/examples/client2.py generated/amot-publisher-subscriber/client2.py

set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" middleware/examples/*Config.py

all:
	$(MAKE) server
	$(MAKE) publisher
	$(MAKE) subscriber
	$(MAKE) publisher_subscriber

run-server:
	cd generated/amot-server && python3 AMoTEngine.py

run-publisher:
	cd generated/amot-publisher && python3 AMoTEngine.py

run-subscriber:
	cd generated/amot-subscriber && python3 AMoTEngine.py

run-published-subscriber:
	cd generated/amot-publisher-subscriber && python3 AMoTEngine.py