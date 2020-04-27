server:
	mkdir -p AMoTBroker
	rm -rf AMoTBroker/*
	cp middleware/examples/AMoTServerAdl.py AMoTBroker/AMoTAdl.py
	cp AMoTEngine.py AMoTBroker/
	cp pickle.py AMoTBroker/
	cp broker-server/AMoTBroker.py AMoTBroker/
	cp middleware/Invoker.py AMoTBroker/
	cp middleware/ServerRequestHandler.py AMoTBroker/


publisher:
	mkdir -p AMoTPublisher
	rm -rf AMoTPublisher/*
	cp middleware/examples/AMoTPublisherAdl.py AMoTPublisher/AMoTAdl.py
	cp AMoTEngine.py AMoTPublisher/
	cp pickle.py AMoTPublisher/
	cp middleware/Requestor.py AMoTPublisher/
	cp middleware/ClientRequestHandler.py AMoTPublisher/
	cp middleware/ClientProxy.py AMoTPublisher/
	cp middleware/examples/AMoTPublisherApp.py AMoTPublisher/AMoTClient.py

subscriber:
	mkdir -p AMoTSubscriber
	rm -rf AMoTSubscriber/*
	cp middleware/examples/AMoTSubscriberAdl.py AMoTSubscriber/AMoTAdl.py
	cp AMoTEngine.py AMoTSubscriber/
	cp pickle.py AMoTSubscriber/
	cp middleware/Invoker.py AMoTSubscriber/
	cp middleware/ServerRequestHandler.py AMoTSubscriber/
	cp middleware/Requestor.py AMoTSubscriber/
	cp middleware/ClientRequestHandler.py AMoTSubscriber/
	cp middleware/ClientProxy.py AMoTSubscriber/
	cp middleware/examples/AMoTSubscriberApp.py AMoTSubscriber/AMoTApp.py

all:
	$(MAKE) server
	$(MAKE) publisher
	$(MAKE) subscriber