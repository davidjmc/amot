broker:
	mkdir -p generated/amot-broker
	rm -rf generated/amot-broker/*
	mkdir -p generated/amot-broker/components

	cp AMoTEngine.py generated/amot-broker/
	cp AMoTAgent.py generated/amot-broker/
	cp main.py generated/amot-broker/main.py

	cp examples/brokerConfig.py generated/amot-broker/config.py


subscriber:
	mkdir -p generated/amot-subscriber
	rm -rf generated/amot-subscriber/*
	mkdir -p generated/amot-subscriber/components

	cp AMoTEngine.py generated/amot-subscriber/
	cp AMoTAgent.py generated/amot-subscriber/
	cp main.py generated/amot-subscriber/main.py

	cp examples/subscriberConfig.py generated/amot-subscriber/config.py


publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*
	mkdir -p generated/amot-publisher/components

	cp AMoTEngine.py generated/amot-publisher/
	cp AMoTAgent.py generated/amot-publisher/
	cp main.py generated/amot-publisher/main.py

	cp examples/publisherConfig.py generated/amot-publisher/config.py


publisher-2:
	mkdir -p generated/amot-publisher2
	rm -rf generated/amot-publisher2/*
	mkdir -p generated/amot-publisher2/components

	cp AMoTEngine.py generated/amot-publisher2/
	cp AMoTAgent.py generated/amot-publisher2/
	cp main.py generated/amot-publisher2/main.py

	cp examples/publisherConfig2.py generated/amot-publisher2/config.py


set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" examples/*Config.py


all:
	mkdir -p generated
	rm -rf generated/*
	$(MAKE) broker
	$(MAKE) publisher
	$(MAKE) publisher-2
	$(MAKE) subscriber

run-broker:
	cd generated/amot-broker && python3 main.py

run-server:
	cd amot-server && npm install && nodemon index.js

run-subscriber:
	cd generated/amot-subscriber && python3 main.py

run-publisher:
	cd generated/amot-publisher && python3 main.py

run-publisher2:
	cd generated/amot-publisher2 && python3 main.py