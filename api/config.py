# api/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///legal_research.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
