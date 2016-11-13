# -*- encoding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db.sqlite", echo=True)
DocumentBase = declarative_base()

from cloudpua import pua
