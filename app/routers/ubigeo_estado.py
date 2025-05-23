from fastapi import APIRouter
from app.db.schema.ubigeo_estado import UbigeoEstado, UbigeoEstadoConsulta  
from app.crud.ubigeo_estado import (registrar_ubigeo_estado as registrar_ubigeo_estado_crud, 
                                    obtener_ubigeo_estado as obtener_ubigeo_estado_crud, 
                                    actualizar_ubigeo_estado as actualizar_ubigeo_estado_crud                                   
                                    )


router = APIRouter(prefix="/ubigeo_estado", tags=["UbigeoEstado"])


@router.post("/registrar", response_model=UbigeoEstado)
def registrar_ubigeo_estado(ubigeo_estado: UbigeoEstadoConsulta):
    
    return registrar_ubigeo_estado_crud(ubigeo_estado)


@router.get("/obtener/{id_UbigeoEstado}", response_model=UbigeoEstado)
def obtener_ubigeo_estado(id_UbigeoEstado:int):
    
    return obtener_ubigeo_estado_crud(id_UbigeoEstado)

@router.put("/actualizar/{id_ubigeo_estado}", response_model=UbigeoEstado)
def actualiza_ubigeo_estado(id_UbigeoEstado:int, ubigeo_estado: UbigeoEstadoConsulta):
    
    return actualizar_ubigeo_estado_crud(id_UbigeoEstado, ubigeo_estado)