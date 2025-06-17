from app.db.conect import SessionLocal
from app.db.models.empleado import Empleado
from app.db.models.empleado_asignacion import EmpleadoAsignacion
from sqlalchemy import text
from fastapi import HTTPException

def registrar_empleado(empleado):

    db = SessionLocal()
    try:
        #Id_Empleado = db.query(Empleado).count() + 1
        db_empleado = Empleado(
        #    Id_Empleado=Id_Empleado,
            Nombre=empleado.Nombre,
            Apellido=empleado.Apellido,
            id_rol=empleado.id_rol,
            correo=empleado.correo
        )
        db.add(db_empleado)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar el empleado: {str(e)}")
    finally:
        db.close()

def obtener_empleado(Id_Empleado: int):

    db = SessionLocal()

    try:
        query = text("SELECT Nombre, Apellido, id_rol, correo From Empleado where Id_Empleado = :Id_Empleado")
        result = db.execute(query, {"Id_Empleado": Id_Empleado})
        result = result.fetchone()  # Obtiene una sola fila del resultado
        if result:
            result = result._mapping  # Convierte el resultado a un diccionario        
            return result
        else:
            raise HTTPException(status_code=404, detail="No se encontró el empleado con el ID proporcionado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el empleado: {str(e)}")
    finally:
        db.close()


def actualizar_empleado(Id_Empleado: int, empleado ):
    db = SessionLocal()

    try:
        db_empleado = db.query(Empleado).filter(Empleado.Id_Empleado == Id_Empleado).first()
        if not db_empleado:
            raise HTTPException(status_code=404, detail="No se encontró el empleado con el ID proporcionado")
        db_empleado.Nombre = empleado.Nombre
        db_empleado.Apellido = empleado.Apellido
        db_empleado.id_rol = empleado.id_rol
        db_empleado.correo = empleado.correo
        db.commit()
        db.refresh(db_empleado)
        #db_empleado = empleado_schema(db_empleado)
        return db_empleado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el empleado: {str(e)}")
    
    finally:
        db.close()

def obtener_ultimo_empleado():
    db = SessionLocal()

    try:

        #db_ultimo_empleado = db.query(Empleado).order_by(Empleado.Id_Empleado.desc()).first()
        db_ultimo_empleado = db.query(Empleado).join(
            EmpleadoAsignacion, Empleado.Id_Empleado == EmpleadoAsignacion.id_Empleado
        ).order_by(Empleado.Id_Empleado.desc()).first()
        if not db_ultimo_empleado:
           raise HTTPException(status_code=404, detail="No se encontró el último empleado registrado")         
        return db_ultimo_empleado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el último empleado:  {str(e)}")
    finally:
        db.close()
