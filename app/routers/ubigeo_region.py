from fastapi import APIRouter
from app.db.schema.ubigeo_region import UbigeoRegion, UbigeoRegionConsulta
from app.crud.ubigeo_region import (registrar_ubigeo_region as registrar_ubigeo_region_crud,
                                    actualizar_ubigeo_region as actualizar_ubigeo_region_crud,
                                    obtener_ubigeo_region as obtener_ubigeo_region_crud)

router = APIRouter(prefix="/ubigeo_region", tags=["UbigeoRegion"])

@router.post("/registrar", response_model=UbigeoRegion)
def registrar_ubigeo_region(ubigeo_region: UbigeoRegionConsulta):
    return registrar_ubigeo_region_crud(ubigeo_region)



@router.get("/obtener/{id_Ubigeo}", response_model=UbigeoRegionConsulta)
def obtener_ubigeo_region(id_Ubigeo: int):
    return obtener_ubigeo_region_crud(id_Ubigeo)

@router.put("/actualizar/{id_Ubigeo}", response_model=UbigeoRegionConsulta)
def actualizar_ubigeo_region(id_Ubigeo: int, ubigeo_region: UbigeoRegionConsulta):
    return actualizar_ubigeo_region_crud(id_Ubigeo, ubigeo_region)