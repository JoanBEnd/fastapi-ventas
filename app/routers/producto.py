from fastapi import APIRouter
from app.db.schema.producto import Producto, ProductoConsulta
from app.crud.producto import (
    registrar_producto as registrar_producto_db, 
    obtener_producto as obtener_producto_db, 
    actualizar_producto as actualizar_producto_db,
    obtener_ultimo_producto as obtener_ultimo_producto_db
)
router = APIRouter(prefix="/productos", tags=["Productos"], responses= {"404": {"description": "Not found"}})

@router.post("/registrar", response_model=Producto)
def registrar_producto(producto: ProductoConsulta):
    return registrar_producto_db(producto)

@router.get("/obtener/{Id_Producto}", response_model=ProductoConsulta)
def obtener_producto(Id_Producto: int):
    return obtener_producto_db(Id_Producto)

@router.put("/actualizar", response_model=ProductoConsulta)
def actualizar_producto(Id_Producto: int, producto: ProductoConsulta):
    return actualizar_producto_db(Id_Producto, producto)

@router.get("/ultimo", response_model=Producto)
def obtener_ultimo_producto():
    return obtener_ultimo_producto_db()