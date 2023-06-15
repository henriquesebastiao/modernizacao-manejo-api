from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.controllers.cargo import CargoController
from app.errors import erros
from app.schemas.cargo import CargoCreateSchema, CargoSchema

router = APIRouter(prefix="/cargo", tags=["Cargo"])


@router.post("/", response_model=CargoSchema, status_code=201,
             responses=erros["status_code"])
async def create(cargo: CargoCreateSchema,
                 service: CargoController = Depends(CargoController)):
    resp = service.create(cargo)
    return JSONResponse(status_code=resp, content=erros["status_code"][resp])


@router.get("/{cargo_id}", response_model=CargoSchema)
def get(cargo_id: int, service: CargoController = Depends(CargoController)):
    resp = service.get_by_id(cargo_id)
    return JSONResponse(resp)
