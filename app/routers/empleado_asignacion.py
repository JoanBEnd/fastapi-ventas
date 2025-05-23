from fastapi import APIRouter
from app.crud.empleado_asignacion import (
    registrar_empleado_asignacion as registrar_empleado_asignacion_db,
    obtener_empleado_asignacion as obtener_empleado_asignacion_db,
    actualizar_empleado_asignacion as actualizar_empleado_asignacion_db
)
from app.db.schema.empleado_asignacion import(
    EmpleadoAsignacion,
    EmpleadoAsignacionConsulta
)

router = APIRouter(prefix="/empleado_asignacion", tags=["Empleado_Asignacion"], responses={404: {"description": "Not found"}})


@router.post("/registrar", response_model=EmpleadoAsignacion)
def registrar(empleado_asignacion: EmpleadoAsignacionConsulta):
    return registrar_empleado_asignacion_db(empleado_asignacion)


@router.get("/{id_Asignacion}", response_model=EmpleadoAsignacionConsulta)
def obtener_empleado_asignacion(id_Asignacion: int):
    return obtener_empleado_asignacion_db(id_Asignacion)


@router.put("/actualizar", response_model=EmpleadoAsignacionConsulta)
def actualizar_empleado_asignacion(id_Asignacion:int, empleado_asignacion: EmpleadoAsignacionConsulta):
    return actualizar_empleado_asignacion_db(id_Asignacion, empleado_asignacion)
