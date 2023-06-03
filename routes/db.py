from fastapi import APIRouter

from database.db import engine
from models.base import Base

router = APIRouter()


@router.delete("/delete")
async def delete_db():
    Base.metadata.drop_all(bind=engine)
    return {"message": "ok"}
