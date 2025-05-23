from app.db.conect import SessionLocal
from app.db.models.roles import roles
from fastapi import HTTPException


def registrar_rol(rol):
    db = SessionLocal()

    try:
        db_rol = Roles(
            rol = rol.cargo
        )
        db.add(db_rol)
        db.commit()
        db.refresh(db_rol)
        return db_rol
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error al registrar el rol: {str(e)}")

    finally:
        db.close()


def obtener_rol(id_rol: int):
    db = SessionLocal()
    try:
        db_rol = db.query(roles).filter(roles.id_rol == id_rol).first()
        if not db_rol:
            raise HTTPException(status_code=404, detail="No se encontró el rol con el ID proporcionado")
        
        return db_rol

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}") 

    finally:
        db.close()


def actualizar_rol(id_rol: int, rol):
    db = SessionLocal()
    try:
        db_rol = db.query(roles).filter(roles.id_rol == id_rol).first()
        if not db_rol:
            raise HTTPException(status_code = 404, detail="No se encontró el rol con el ID proporcionado")

        db_rol.cargo = rol.cargo

        db.commit()
        db.refresh(db_rol)
        return db_rol
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")
    
    finally:
        db.close()