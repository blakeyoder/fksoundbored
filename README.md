# Fictive Kin Soundbored™
Re-live the 90s with this Fictive Kin inspired soundboard. There might even be a perfect prank call buried in the permutations on this board. Currently, the production site is hosted [here](https://ao5h38vfn1.execute-api.us-east-1.amazonaws.com/dev/)

# Adding more sounds to the board
To get a new sound added to the board, please open an issue with 1. The name of the button 2. A link to the soundfile, and 3. Express written consent given if someone other than you is featured in the soundclip

## Quick Start

Run the application:

    make run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Prerequisites

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev


## Development environment and release process

 - create virtualenv with Flask and FK-Soundbored installed into it (latter is installed in
   [develop mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) which allows
   modifying source code directly without a need to re-install the app): `make venv`

 - run development server in debug mode: `make run`; Flask will restart if source code is modified

 - run tests: `make test` (see also: [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/))

 - create source distribution: `make sdist` (will run tests first)

 - to remove virtualenv and built distributions: `make clean`

 - to add more python dependencies: add to `install_requires` in `setup.py`

 - to modify configuration in development environment: edit file `settings.cfg`; this is a local configuration file
   and it is *ignored* by Git - make sure to put a proper configuration file to a production environment when
   deploying

