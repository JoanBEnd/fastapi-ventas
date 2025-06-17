from fastapi import APIRouter
from app.db.schema.empleado import Empleado, EmpleadoConsulta
from app.crud.empleado import (registrar_empleado as registrar_empleado_db, 
                               obtener_empleado as obtener_empleados_db, 
                               actualizar_empleado as actualizar_empleado_db,
                               obtener_ultimo_empleado as obtener_ultimo_empleado_db)

router = APIRouter(prefix="/empleados", tags=["Empleados"], responses={404: {"description": "Not found"}})


@router.post("/registrar", response_model=Empleado)
def registrar_empleado(empleado: EmpleadoConsulta) :    
    return registrar_empleado_db(empleado)


@router.get("/obtener/{Id_Empleado}", response_model=EmpleadoConsulta)
def obtener_empleado(Id_Empleado: int):
    return obtener_empleados_db(Id_Empleado)

@router.put("/actualizar", response_model=EmpleadoConsulta)
def actualizar_empleado(Id_Empleado: int, empleado: EmpleadoConsulta):
    return actualizar_empleado_db(Id_Empleado, empleado)

@router.get("/ultimo", response_model=Empleado)
def obtener_ultimo_empleado():
    return obtener_ultimo_empleado_db()