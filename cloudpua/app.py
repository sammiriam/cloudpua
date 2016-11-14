# -*- encoding: utf-8 -*-
"""Createing app"""

from flask import Flask
from .db import configure as db_configure


def create_app():
    """create the flask app"""
    app = Flask("cloudpua")
    app.config.from_pyfile('settings.py')
    db_configure(app)
    from .url import url_blueprint
    app.register_blueprint(url_blueprint)
    return app
