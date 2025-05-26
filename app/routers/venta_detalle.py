from fastapi import APIRouter
from app.db.schema.venta_detalle import venta_detalle, venta_detalleConsulta, venta_detalleUpdate
from app.crud.venta_detalle import (
    registrar_venta_detalle as registrar_venta_detalle_crud,
    actualizar_venta_detalle as actualizar_venta_detalle_crud,
    obtener_venta_detalle as obtener_venta_detalle_crud    
    )

router = APIRouter(prefix="/venta_detalle", tags=["Venta Detalle"])

@router.post("/registrar", response_model=venta_detalle)
def registrar_venta_detalle(ventaDetalle: venta_detalleConsulta):
    return registrar_venta_detalle_crud(ventaDetalle)

@router.get("/obtener/{Transaccion_ID}", response_model=venta_detalleConsulta)
def obtener_venta_detalle(Transaccion_ID: int):
    return obtener_venta_detalle_crud(Transaccion_ID)

@router.put("/actualizar/{Transaccion_ID}", response_model=venta_detalleConsulta)
def actualizar_venta_detalle(Transaccion_ID: int, ventaDetalle:venta_detalleUpdate):
    return actualizar_venta_detalle_crud(Transaccion_ID, ventaDetalle)
