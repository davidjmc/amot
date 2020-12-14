broker:
	mkdir -p generated/amot-broker
	rm -rf generated/amot-broker/*
	mkdir -p generated/amot-broker/components

	cp AMoTEngine.py generated/amot-broker/
	cp AMoTAgent.py generated/amot-broker/
	cp main.py generated/amot-broker/main.py

	cp examples/serverAdl.py generated/amot-broker/adl.py
	cp examples/serverConfig.py generated/amot-broker/config.py
	cp examples/server.txt generated/amot-broker/versions.txt


subscriber:
	mkdir -p generated/amot-subscriber
	rm -rf generated/amot-subscriber/*
	mkdir -p generated/amot-subscriber/components

	cp AMoTEngine.py generated/amot-subscriber/
	cp AMoTAgent.py generated/amot-subscriber/
	cp main.py generated/amot-subscriber/main.py

	cp examples/subscriberAdl.py generated/amot-subscriber/adl.py
	cp examples/subscriberConfig.py generated/amot-subscriber/config.py
	cp examples/subscriber.txt generated/amot-subscriber/versions.txt


publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*
	mkdir -p generated/amot-publisher/components

	cp AMoTEngine.py generated/amot-publisher/
	cp AMoTAgent.py generated/amot-publisher/
	cp main.py generated/amot-publisher/main.py

	cp examples/thinAdl.py generated/amot-publisher/adl.py
	cp examples/thinConfig.py generated/amot-publisher/config.py
	cp examples/publisher.txt generated/amot-publisher/versions.txt


publisher-2:
	mkdir -p generated/amot-publisher2
	rm -rf generated/amot-publisher2/*
	mkdir -p generated/amot-publisher2/components

	cp AMoTEngine.py generated/amot-publisher2/
	cp AMoTAgent.py generated/amot-publisher2/
	cp main.py generated/amot-publisher2/main.py

	cp examples/thinAdl2.py generated/amot-publisher2/adl.py
	cp examples/thinConfig2.py generated/amot-publisher2/config.py
	cp examples/publisher.txt generated/amot-publisher2/versions.txt


set:
	sed -i "s/'host':.*/'host': b'$(IP)',/g" middleware/examples/*Config.py


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
	cd amot-server && nodemon index.js

run-subscriber:
	cd generated/amot-subscriber && python3 main.py

run-publisher:
	cd generated/amot-publisher && python3 main.py

run-publisher2:
	cd generated/amot-publisher2 && python3 main.py