from app.db.conect import SessionLocal
from app.db.models.empleado_asignacion import EmpleadoAsignacion
from fastapi import HTTPException

def registrar_empleado_asignacion(empleadoAsignacion):
    db = SessionLocal()
    try:
        db_empleado_Asignacion = EmpleadoAsignacion(
            id_Empleado = empleadoAsignacion.id_Empleado,
            id_UbigeoPermiso = empleadoAsignacion.id_UbigeoPermiso,
            Ubigeo_Descripcion = empleadoAsignacion.Ubigeo_Descripcion
        )

        db.add(db_empleado_Asignacion)
        db.commit()
        db.refresh(db_empleado_Asignacion)
        return db_empleado_Asignacion
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar la asignacion del empleado: {str(e)}")

    finally:
        db.close()


def obtener_empleado_asignacion(id_Asignacion: int):
    db = SessionLocal()
    try:
        db_empleado_Asignacion = db.query(EmpleadoAsignacion).filter(EmpleadoAsignacion.id_Asignacion == id_Asignacion).first()
        if not db_empleado_Asignacion:
            raise HTTPException(status_code=404, detail="No se encontró la asignación del empleado con el ID proporcionado")
        return db_empleado_Asignacion
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la asignación del empleado: {str(e)}")

    finally:
        db.close()


def actualizar_empleado_asignacion(id_Asignacion: int, empleadoAsignacion):
    db = SessionLocal() 
    try:
        db_empleado_Asignacion = db.query(EmpleadoAsignacion).filter(EmpleadoAsignacion.id_Asignacion == id_Asignacion).first()
        if not db_empleado_Asignacion:
            raise HTTPException(status_code=404, detail="No se encontró la asignación del empleado con el ID proporcionado")
        db_empleado_Asignacion.id_empleado = empleadoAsignacion.id_Empleado
        db_empleado_Asignacion.id_UbigeoPermiso = empleadoAsignacion.id_UbigeoPermiso
        db_empleado_Asignacion.Ubigeo_Descripcion = empleadoAsignacion.Ubigeo_Descripcion

        db.commit()
        db.refresh(db_empleado_Asignacion)
        return db_empleado_Asignacion
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la asignación del empleado: {str(e)}")
    finally:
        db.close()