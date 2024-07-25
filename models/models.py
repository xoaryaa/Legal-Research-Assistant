# models/models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Case(Base):
    __tablename__ = 'cases'
    case_id = Column(Integer, primary_key=True)
    case_name = Column(String)
    court = Column(String)
    decision_date = Column(Date)
    summary = Column(Text)

class Law(Base):
    __tablename__ = 'laws'
    law_id = Column(Integer, primary_key=True)
    law_name = Column(String)
    description = Column(Text)
    jurisdiction = Column(String)

class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    client_name = Column(String)
    contact_info = Column(Text)

class ResearchNote(Base):
    __tablename__ = 'research_notes'
    note_id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'))
    note = Column(Text)
    created_at = Column(Date, default='CURRENT_TIMESTAMP')

engine = create_engine('sqlite:///legal_research.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
