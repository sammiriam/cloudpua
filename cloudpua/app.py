# -*- encoding: utf-8 -*-
"""Createing app"""

from flask import Flask


def create_app():
    """create the flask app"""
    app = Flask("cloudpua")
    from .url import url_blueprint
    app.register_blueprint(url_blueprint)
    return app
