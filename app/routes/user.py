from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.base_controller import BaseControllers
from app.controllers.usuario_controller import UserController
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreateSchema, UserLoginSchema, \
    UserSchema, UserUpdateSchema

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=201)
async def create(user: UserCreateSchema, db: Session = Depends(get_db)):
    controller = BaseControllers(db, User)
    if controller.create(user):
        return {"mensagem": "Criado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.get("/{id}", response_model=UserSchema)
def get(user_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, User)
    if response := controller.get_by_id(user_id):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.post("/login")
def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    controller = UserController(db, User)
    if response := controller.login(user):
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro criado")


@router.get("/", response_model=list[UserSchema])
async def get_all(db: Session = Depends(get_db)):
    controller = BaseControllers(db, User)
    if response := controller.get_all():
        return response
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.patch("/{id}")
async def update(user_id: int, user: UserUpdateSchema,
                 db: Session = Depends(get_db)):
    controller = BaseControllers(db, User)
    if controller.update(user_id, user):
        return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")


@router.delete("/{id}")
async def delete(user_id: int, db: Session = Depends(get_db)):
    controller = BaseControllers(db, User)
    if controller.delete(user_id):
        return {"mensagem": "Apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
