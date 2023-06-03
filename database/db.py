from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'postgresql://postgres:postgres@localhost:5432/db-manejo?sslmode=disable'

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
