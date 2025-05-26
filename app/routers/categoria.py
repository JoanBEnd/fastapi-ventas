from fastapi import APIRouter
from app.crud.categoria import (
    registrar_categoria as registrar_categoria_db, 
    obtener_categoria as obtener_categoria_db, 
    actualizar_categoria as actualizar_categoria_db,
    obtener_ultimo_registro as obtener_ultimo_registro_crud
    )
from app.db.schema.categoria import Categoria, CategoriaConsulta

router = APIRouter(prefix="/categoria", tags=["Categoria"], responses={404: {"description": "Not found"}})



@router.get("/obtener/{id_Categoria}", response_model=CategoriaConsulta)
def obtener_categoria(id_Categoria: int):
    return obtener_categoria_db(id_Categoria)

@router.post("/registrar", response_model=Categoria)
def registrar_categoria(categoria: CategoriaConsulta):
    return registrar_categoria_db(categoria)

@router.put("/actualizar", response_model=CategoriaConsulta)
def actualizar_categoria(id_Categoria: int, categoria: CategoriaConsulta):
    return actualizar_categoria_db(id_Categoria, categoria)

@router.get("/ultimo", response_model=Categoria)
def obtener_ultimo_registro():
    return obtener_ultimo_registro_crud()


