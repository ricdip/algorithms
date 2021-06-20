.POSIX:

PYTHON ?= python3
PIP ?= pip

.DEFAULT_GOAL: help


.SILENT: help
help:
	printf "%s \\t\\t %s\n" "help" "show this help message"
	printf "%s \\t\\t %s\n" "all" "init, install and run"
	printf "%s \\t\\t %s\n" "init" "create Python venv"
	printf "%s \\t %s\n" "install" "install requirements"
	printf "%s \\t\\t %s\n" "run" "run main.py"
	printf "%s \\t\\t %s\n" "clean" "clean venv"


all: install run


init:
	$(PYTHON) -m venv venv


.ONESHELL:
install: init
	. venv/bin/activate
	$(PIP) install -r requirements.txt


.ONESHELL:
run: venv
	. venv/bin/activate
	$(PYTHON) main.py


clean: venv
	rm -rf venv


.PHONY: help all init install run clean
