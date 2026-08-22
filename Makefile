PYTHON ?= python

.PHONY: install download prepare database test notebook pipeline

install:
	$(PYTHON) -m pip install -r requirements-dev.txt

download:
	$(PYTHON) src/download_data.py

prepare:
	$(PYTHON) src/prepare_data.py

database:
	$(PYTHON) src/build_database.py

test:
	$(PYTHON) -m pytest -q

notebook:
	jupyter notebook notebooks/01_eda.ipynb

pipeline: download prepare database
