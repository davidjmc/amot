set:
	sed -i "s/_HOST=.*/_HOST=$(IP)/g" examples/**/env.ini

publisher:
	mkdir -p generated/amot-publisher/
	rm -rf generated/amot-publisher/*
	mkdir -p generated/amot-publisher/components/

	cp AMoTEngine.py generated/amot-publisher/
	cp AMoTAgent.py generated/amot-publisher/
	cp main.py generated/amot-publisher/main.py

	cp examples/publisher/app.py generated/amot-publisher/
	cp examples/publisher/config.py generated/amot-publisher/
	cp examples/publisher/env.ini generated/amot-publisher/


subscriber:
	mkdir -p generated/amot-subscriber/
	rm -rf generated/amot-subscriber/*
	mkdir -p generated/amot-subscriber/components/

	cp AMoTEngine.py generated/amot-subscriber/
	cp AMoTAgent.py generated/amot-subscriber/
	cp main.py generated/amot-subscriber/main.py

	cp examples/subscriber/app.py generated/amot-subscriber/
	cp examples/subscriber/config.py generated/amot-subscriber/
	cp examples/subscriber/env.ini generated/amot-subscriber/


broker:
	mkdir -p generated/amot-broker/
	rm -rf generated/amot-broker/*
	mkdir -p generated/amot-broker/components/

	cp AMoTEngine.py generated/amot-broker/
	cp AMoTAgent.py generated/amot-broker/
	cp main.py generated/amot-broker/main.py

	cp examples/broker/app.py generated/amot-broker/
	cp examples/broker/config.py generated/amot-broker/
	cp examples/broker/env.ini generated/amot-broker/


all:
	$(MAKE) broker
	$(MAKE) publisher
	$(MAKE) subscriber


run-publisher:
	cd generated/amot-publisher && python3 main.py

run-subscriber:
	cd generated/amot-subscriber && python3 main.py

run-broker:
	cd generated/amot-broker && python3 main.py