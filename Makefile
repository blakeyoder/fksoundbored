all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP=fksoundbored FLASK_DEBUG=1 FKSOUNDBORED_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	FKSOUNDBORED_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
