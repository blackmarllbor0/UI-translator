.PHONY: init_venv
init_venv:
	source venv/bin/activate

.PHONY: run
run:
	python main.py

.PHONY: lint
lint:
	black .