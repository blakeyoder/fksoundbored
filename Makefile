all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP=fksoundbored CONFIG_PATH=fksoundbored.config.DevConfig venv/bin/flask run

sdist: venv test
	venv/bin/python setup.py sdist
