from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost:5432/db-manejo?sslmode=disable')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    origem = Column(String)
    id_mae = Column(Integer)
    id_pai = Column(Integer)
    idade = Column(Integer)
    sexo = Column(String)
    data_entrada = Column(Date)
    peso_nascimento = Column(Integer)

