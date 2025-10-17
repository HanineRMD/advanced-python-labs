# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# CHANGE : remplace USERNAME/PASSWD par ton user/password
URL_DATABASE = 'postgresql://quizuser:changeme@localhost:5432/quizapp'

engine = create_engine(URL_DATABASE, echo=False)  # echo=True pour debug SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
