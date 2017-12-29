import os
from flask import Flask


def create_app(object_name):
    app = Flask(__name__)

    app.config.from_object(object_name)

    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
        file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'fksoundbored.log'), 'midnight')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
        app.logger.addHandler(file_handler)

    return app

app = create_app(os.environ.get('CONFIG_PATH'))


import fksoundbored.views
