server:
	mkdir -p generated/amot-server
	rm -rf generated/amot-server/*

	cp AMoTEngine.py generated/amot-server/
	cp Executor.py generated/amot-server/
	cp pickle.py generated/amot-server/

	cp middleware/examples/serverAdl.py generated/amot-server/adl.py
	cp middleware/examples/serverConfig.py generated/amot-server/config.py
	cp middleware/examples/server.txt generated/amot-server/versions.txt

	cp queue-server/NotificationConsumer.py generated/amot-server/
	cp queue-server/NotificationEngine.py generated/amot-server/
	cp queue-server/SubscriptionManager.py generated/amot-server/
	cp queue-server/NotifierProxy.py generated/amot-server/

	cp middleware/ServerRequestHandler.py generated/amot-server/
	cp middleware/ClientRequestHandler.py generated/amot-server/
	cp middleware/QueueProxy.py generated/amot-server/
	cp middleware/Marshaller.py generated/amot-server/
	cp middleware/UnmarshallerHybrid.py generated/amot-server/

adaptation_manager:
	mkdir -p generated/amot-adaptation-manager
	rm -rf generated/amot-adaptation-manager/*

	cp AMoTEngine.py generated/amot-adaptation-manager/
	cp Executor.py generated/amot-adaptation-manager/
	cp pickle.py generated/amot-adaptation-manager/

	cp middleware/examples/adapterAdl.py generated/amot-adaptation-manager/adl.py
	cp middleware/examples/adapterConfig.py generated/amot-adaptation-manager/config.py
	cp middleware/examples/adapter.txt generated/amot-adaptation-manager/versions.txt

	cp adaptation-manager/AdaptationEngine.py generated/amot-adaptation-manager/
	cp adaptation-manager/EvolutiveAdapter.py generated/amot-adaptation-manager/
	cp adaptation-manager/EvolutiveMonitor.py generated/amot-adaptation-manager/
	cp adaptation-manager/EvolutiveAnaliser.py generated/amot-adaptation-manager/
	cp adaptation-manager/EvolutiveExecutor.py generated/amot-adaptation-manager/
	cp -R adaptation-manager/library generated/amot-adaptation-manager/

	cp middleware/ServerRequestHandler.py generated/amot-adaptation-manager/
	cp middleware/UnmarshallerHybrid.py generated/amot-adaptation-manager/

publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*

	cp AMoTEngine.py generated/amot-publisher/
	cp Executor.py generated/amot-publisher/
	cp pickle.py generated/amot-publisher/

	cp middleware/examples/publisherAdl.py generated/amot-publisher/adl.py
	cp middleware/examples/publisherConfig.py generated/amot-publisher/config.py
	cp middleware/examples/publisher.txt generated/amot-publisher/versions.txt
	cp middleware/examples/publisherApp.py generated/amot-publisher/Client.py

	cp middleware/ClientRequestHandler.py generated/amot-publisher/
	cp middleware/QueueProxy.py generated/amot-publisher/
	cp middleware/Marshaller.py generated/amot-publisher/
	cp middleware/AdaptationProxy.py generated/amot-publisher/

subscriber:
	mkdir -p generated/amot-subscriber
	rm -rf generated/amot-subscriber/*

	cp AMoTEngine.py generated/amot-subscriber/
	cp Executor.py generated/amot-subscriber/

	cp middleware/examples/subscriberAdl.py generated/amot-subscriber/adl.py
	cp middleware/examples/subscriberConfig.py generated/amot-subscriber/config.py
	cp middleware/examples/subscriber.txt generated/amot-subscriber/versions.txt
	cp middleware/examples/subscriberApp.py generated/amot-subscriber/App.py

	cp middleware/ServerRequestHandler.py generated/amot-subscriber/
	cp middleware/ClientRequestHandler.py generated/amot-subscriber/
	cp middleware/QueueProxy.py generated/amot-subscriber/
	cp middleware/Marshaller.py generated/amot-subscriber/
	cp middleware/Unmarshaller.py generated/amot-subscriber/
	cp middleware/Notifier.py generated/amot-subscriber/
	cp middleware/Subscriptor.py generated/amot-subscriber/
	cp middleware/AdaptationProxy.py generated/amot-subscriber/

publisher_subscriber:
	mkdir -p generated/amot-publisher-subscriber
	rm -rf generated/amot-publisher-subscriber/*

	cp AMoTEngine.py generated/amot-publisher-subscriber/
	cp Executor.py generated/amot-publisher-subscriber/


set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" middleware/examples/*Config.py

all:
	$(MAKE) server
	$(MAKE) adaptation_manager
	$(MAKE) publisher
	$(MAKE) subscriber
	$(MAKE) publisher_subscriber

run-server:
	cd generated/amot-server && python3 AMoTEngine.py

run-adaptation-manager:
	cd generated/amot-adaptation-manager && python3 AMoTEngine.py

run-publisher:
	cd generated/amot-publisher && python3 AMoTEngine.py

run-subscriber:
	cd generated/amot-subscriber && python3 AMoTEngine.py

run-published-subscriber:
	cd generated/amot-publisher-subscriber && python3 AMoTEngine.py
