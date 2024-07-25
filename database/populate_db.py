# populate_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Case, Law, Client, ResearchNote, Base

engine = create_engine('sqlite:///legal_research.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add initial data
new_case = Case(case_name='Case Example', court='Supreme Court', decision_date='2022-01-01', summary='Summary of the case.')
session.add(new_case)
session.commit()
