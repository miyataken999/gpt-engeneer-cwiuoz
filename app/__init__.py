from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

engine = create_engine('sqlite:///usersystem.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()