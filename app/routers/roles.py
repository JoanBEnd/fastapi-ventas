from fastapi import APIRouter
from app.crud.roles import registrar_rol as registrar_rol_db, obtener_rol as obtener_rol_db, actualizar_rol as actualizar_rol_db
from app.db.schema.roles import rol, rolConsulta

router = APIRouter(prefix="/roles", tags=["Roles"], responses={404: {"description": "Not found"}})


@router.get("/{id_rol}", response_model=rolConsulta)
def obtener_rol(id_rol: int):
    return obtener_rol_db(id_rol)


@router.post("/registrar", response_model=rol)
def registrar_rol(rol: rol):
    return registrar_rol_db(rol)


@router.put("/actualizar{id_rol}", response_model=rolConsulta)
def actualizar_rol(id_rol: int, rol: rolConsulta):
    return actualizar_rol_db(id_rol, rol)
