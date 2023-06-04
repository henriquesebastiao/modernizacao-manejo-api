from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'postgresql://postgres:postgres@localhost:5432/db-manejo?sslmode=disable'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

