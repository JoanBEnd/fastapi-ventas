from fastapi import APIRouter
from app.crud.venta import (
    obtener_venta as obtener_venta_crud,
    registrar_venta as registrar_venta_crud,
    actualizar_venta as actualizar_venta_crud
)
from app.db.schema.venta import venta, ventaConsulta


router = APIRouter(prefix="/venta", tags=["venta"])

@router.post("/registrar", response_model=venta)
def registrar_venta(venta: ventaConsulta):
    return registrar_venta_crud(venta)


@router.get("/obtener{Transaccion_ID}", response_model=ventaConsulta)
def obtener_venta(Transaccion_ID: int, venta:ventaConsulta):
    return obtener_venta_crud(Transaccion_ID, venta)


@router.put("/actualizar", response_model=ventaConsulta)
def actualizar_venta(Transaccion_ID: int, venta:ventaConsulta):

    return actualizar_venta_crud(Transaccion_ID, venta)