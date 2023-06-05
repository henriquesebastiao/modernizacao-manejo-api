from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
