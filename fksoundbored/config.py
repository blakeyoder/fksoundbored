# -*- coding: utf-8 -*-


class BaseConfig(object):
    LOG_DIR='fksoundbored/logs'

class DevConfig(BaseConfig):
    DEBUG=True
    FLASK_DEBUG=True

class ProductionConfig(BaseConfig):
    DEBUG=False
    FLASK_DEBUG=False

