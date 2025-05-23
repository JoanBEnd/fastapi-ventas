from fastapi import APIRouter
from app.crud.cliente import obtener_cliente as obtener_cliente_db, actualizar_cliente as actualizar_cliente_db, registrar_cliente as registrar_cliente_db

#from app.db.models.cliente import Cliente
from app.db.schema.cliente import Cliente, ClienteConsulta

router = APIRouter(prefix="/clientes", tags=["Clientes"], responses={404: {"description": "Not found"}})



@router.get("/")
def bienvenida():
    return {"message": "Bienvenido a clientes API"}

@router.get("/{Id_Cliente}", response_model=ClienteConsulta)
def obtener_cliente(Id_Cliente: int): 
    return obtener_cliente_db(Id_Cliente)

@router.post("/registrar", response_model=Cliente)   
def registrar_cliente(cliente: ClienteConsulta):
    return registrar_cliente_db(cliente)  

@router.put("/actualizar", response_model=ClienteConsulta)
def actualizar_cliente(Id_Cliente: int, cliente: ClienteConsulta):
    return actualizar_cliente_db(Id_Cliente, cliente)
     