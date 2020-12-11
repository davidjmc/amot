broker:
	mkdir -p generated/amot-broker
	rm -rf generated/amot-broker/*
	mkdir -p generated/amot-broker/components

	cp AMoTEngine.py generated/amot-broker/
	cp AMoTAgent.py generated/amot-broker/
	cp main.py generated/amot-broker/main.py

	cp middleware/examples/serverAdl.py generated/amot-broker/adl.py
	cp middleware/examples/serverConfig.py generated/amot-broker/config.py
	cp middleware/examples/server.txt generated/amot-broker/versions.txt


subscriber:
	mkdir -p generated/amot-subscriber
	rm -rf generated/amot-subscriber/*
	mkdir -p generated/amot-subscriber/components

	cp AMoTEngine.py generated/amot-subscriber/
	cp AMoTAgent.py generated/amot-subscriber/
	cp main.py generated/amot-subscriber/main.py

	cp middleware/examples/subscriberAdl.py generated/amot-subscriber/adl.py
	cp middleware/examples/subscriberConfig.py generated/amot-subscriber/config.py
	cp middleware/examples/subscriber.txt generated/amot-subscriber/versions.txt


publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*
	mkdir -p generated/amot-publisher/components

	cp AMoTEngine.py generated/amot-publisher/
	cp AMoTAgent.py generated/amot-publisher/
	cp main.py generated/amot-publisher/main.py

	cp middleware/examples/thinAdl.py generated/amot-publisher/adl.py
	cp middleware/examples/thinConfig.py generated/amot-publisher/config.py
	cp middleware/examples/publisher.txt generated/amot-publisher/versions.txt


set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" middleware/examples/*Config.py


all:
	$(MAKE) broker
	$(MAKE) publisher
	$(MAKE) subscriber

run-broker:
	cd generated/amot-broker && python3 main.py

run-server:
	cd amot-server && nodemon index.js

run-subscriber:
	cd generated/amot-subscriber && python3 main.py

run-publisher:
	cd generated/amot-publisher && python3 main.py