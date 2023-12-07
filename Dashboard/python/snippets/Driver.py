#!/usr/bin/python
import os
import cx_Oracle
import sys
import csv
import datetime
from pathlib import Path
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd 
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
Base = declarative_base()
engine = create_engine('oracle://59857:cD194775@VERIMPRD_DDMA')
con = engine.connect()

class Users(Base):
    __tablename__ = "users"
	BC_SBKD = Column(Integer, primary_key=True)
    BC_MUSNO = Column(Integer, primary_key=True)
    BC_ACILKD1 = Column(String)
    BC_KREDIKOD_MAIN = Column(String)

Borclure.__table__.create(bind=engine, checkfirst=True)