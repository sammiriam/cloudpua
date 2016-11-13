# -*- encoding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

DocumentBase = declarative_base()


def configure(app):
    """为App配置数据库连接设置

    :param app: Flask app
    :type app: flask.Flask
    :return:
    """
    uri = app.config.get('SQLALCHEMY_URI', 'sqlite:///db.sqlite')
    engine = create_engine(uri, echo=app.debug)
    app.config['SQLALCHEMY_ENGINE'] = engine
    Session.configure(bind=engine)


from cloudpua import pua
