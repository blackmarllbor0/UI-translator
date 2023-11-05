.PHONY: run
run:
	python main.py

.PHONY: lint
lint:
	black .

.PHONY: setup
setup:
	pip install .