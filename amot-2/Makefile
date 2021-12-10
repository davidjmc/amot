publisher:
	mkdir -p generated/amot-publisher
	rm -rf generated/amot-publisher/*
	mkdir -p generated/amot-publisher/components

	cp AMoTEngine.py generated/amot-publisher/
	cp AMoTAgent.py generated/amot-publisher/
	cp main.py generated/amot-publisher/main.py

	cp examples/publisher/app.py generated/amot-publisher/
	cp examples/publisher/config.py generated/amot-publisher/
	cp examples/publisher/env.ini generated/amot-publisher/


run-publisher:
	cd generated/amot-publisher && python3 main.py