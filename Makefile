server:
	mkdir -p amot-server
	rm -rf amot-server/*
	cp middleware/examples/serverAdl.py amot-server/adl.py
	cp middleware/examples/serverConfig.py amot-server/config.py
	cp AMoTEngine.py amot-server/
	cp pickle.py amot-server/
	cp queue-server/QueueServer.py amot-server/
	cp middleware/Invoker.py amot-server/
	cp middleware/ServerRequestHandler.py amot-server/
	cp middleware/Requestor.py amot-server/
	cp middleware/ClientRequestHandler.py amot-server/
	cp middleware/ClientProxy.py amot-server/

publisher:
	mkdir -p amot-publisher
	rm -rf amot-publisher/*
	cp middleware/examples/publisherAdl.py amot-publisher/adl.py
	cp middleware/examples/publisherConfig.py amot-publisher/config.py
	cp AMoTEngine.py amot-publisher/
	cp pickle.py amot-publisher/
	cp middleware/Requestor.py amot-publisher/
	cp middleware/ClientRequestHandler.py amot-publisher/
	cp middleware/ClientProxy.py amot-publisher/
	cp middleware/examples/publisherApp.py amot-publisher/Client.py

subscriber:
	mkdir -p amot-subscriber
	rm -rf amot-subscriber/*
	cp middleware/examples/subscriberAdl.py amot-subscriber/adl.py
	cp middleware/examples/subscriberConfig.py amot-subscriber/config.py
	cp AMoTEngine.py amot-subscriber/
	cp pickle.py amot-subscriber/
	cp middleware/Invoker.py amot-subscriber/
	cp middleware/ServerRequestHandler.py amot-subscriber/
	cp middleware/Requestor.py amot-subscriber/
	cp middleware/ClientRequestHandler.py amot-subscriber/
	cp middleware/ClientProxy.py amot-subscriber/
	cp middleware/examples/subscriberApp.py amot-subscriber/App.py

publisher_subscriber:
	mkdir -p amot-publisher-subscriber
	rm -rf amot-publisher-subscriber/*
	cp middleware/examples/publisherSubscriberAdl.py amot-publisher-subscriber/adl.py
	cp engine.py amot-publisher-subscriber/
	cp config.py amot-publisher-subscriber/
	cp pickle.py amot-publisher-subscriber/
	cp middleware/Invoker.py amot-publisher-subscriber/
	cp middleware/ServerRequestHandler.py amot-publisher-subscriber/
	cp middleware/Requestor.py amot-publisher-subscriber/
	cp middleware/ClientRequestHandler.py amot-publisher-subscriber/
	cp middleware/ClientProxy.py amot-publisher-subscriber/
	cp middleware/examples/subscriberApp.py amot-publisher-subscriber/app.py
	cp middleware/examples/client2.py amot-publisher-subscriber/client2.py

set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" middleware/examples/*Config.py

all:
	$(MAKE) server
	$(MAKE) publisher
	$(MAKE) subscriber
# 	$(MAKE) publisher_subscriber

run-server:
	cd amot-server && python3 AMoTEngine.py

run-publisher:
	cd amot-publisher && python3 AMoTEngine.py

run-subscriber:
	cd amot-subscriber && python3 AMoTEngine.py