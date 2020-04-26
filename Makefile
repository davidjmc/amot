server:
	mkdir -p AMoTBroker
	cp AMotAdl.py AMoTBroker/
	cp AMoTEngine.py AMoTBroker/
	cp pickle.py AMoTBroker/
	cp broker-server/AMoTBroker.py AMoTBroker/
	cp middleware/Invoker.py AMoTBroker/
	cp middleware/ServerRequestHandler.py AMoTBroker/


publisher:
	mkdir -p AMoTPublisher
	cp AMotAdl.py AMoTPublisher/
	cp AMoTEngine.py AMoTPublisher/
	cp pickle.py AMoTPublisher/
	cp middleware/Requestor.py AMoTPublisher/
	cp middleware/ClientRequestHandler.py AMoTPublisher/
	cp middleware/ClientProxy.py AMoTPublisher/
	cp middleware/examples/AMoTClient.py AMoTPublisher/

subscriber:
	mkdir -p AMoTSubscriber
	cp AMotAdl.py AMoTSubscriber/
	cp AMoTEngine.py AMoTSubscriber/
	cp pickle.py AMoTSubscriber/
	cp middleware/Requestor.py AMoTSubscriber/
	cp middleware/ClientRequestHandler.py AMoTSubscriber/
	cp middleware/ClientProxy.py AMoTSubscriber/
	cp middleware/examples/AMoTClient.py AMoTSubscriber/