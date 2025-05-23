from fastapi import APIRouter
from app.db.schema.ubigeo_ciudad import UbigeoCiudad, UbigeoCiudadConsulta
from app.crud.ubigeo_ciudad import (
    registrar_ubigeo_ciudad as registrar_ubigeo_ciudad_crud,
    obtener_ubigeo_ciudad as obtener_ubigeo_ciudad_crud,
    actualizar_ubigeo_ciudad as actualizar_ubigeo_ciudad_crud
)


router = APIRouter(prefix="/ubigeo_ciudad", tags=["UbigeoCiudad"])

@router.post("/registrar", response_model=UbigeoCiudad)
def registrar_ubigeo_ciudad(ubigeo_ciudad: UbigeoCiudadConsulta):

    return registrar_ubigeo_ciudad_crud(ubigeo_ciudad)


@router.get("/obtener/{id_UbigeoCiudad}", response_model=UbigeoCiudad)
def obtener_ubigeo_ciudad(id_UbigeoCiudad: int):

    return obtener_ubigeo_ciudad_crud(id_UbigeoCiudad)

@router.put("/actualizar/{id_ubigeo_ciudad}", response_model=UbigeoCiudadConsulta)
def actualiza_ubigeo_ciudad(id_UbigeoCiudad: int, ubigeo_ciudad: UbigeoCiudadConsulta):

    return actualizar_ubigeo_ciudad_crud(id_UbigeoCiudad, ubigeo_ciudad)

