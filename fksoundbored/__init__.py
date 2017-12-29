import os
from flask import Flask


def create_app(object_name):
    app = Flask(__name__)

    app.config.from_object(object_name)

    return app

app = create_app(os.environ.get('CONFIG_PATH'))


import fksoundbored.views
