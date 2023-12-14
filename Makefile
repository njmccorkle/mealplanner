SHELL := /bin/bash

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
  
pip-install-dev:
	pip install --upgrade pip pip-tools
	pip-sync --user requirements-dev.txt

pip-install:
	pip install --upgrade pip pip-tools
	pip-sync --user requirements.txt
  
pip-update:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in
	pip-compile requirements-dev.in
	pip-sync  --user requirements.txt requirements-dev.txt

run:
	python manage.py migrate && python manage.py runserver

dump-sample-data:
	python manage.py dumpdata --exclude=auth --exclude=sessions --exclude=contenttypes --exclude=admin --output sample_data/sample_data.json

restore-sample-data:
	python manage.py loaddata sample_data/sample_data.json
# lint:
# 	flake8 .
# 	mypy .

# black:
# 	python -m black .

cleanimports:
	isort .
#	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports project_name

# clean-lint: cleanimports black lint

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run