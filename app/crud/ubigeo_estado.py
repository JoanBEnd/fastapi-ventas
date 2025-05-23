from fastapi import HTTPException
from app.db.conect import SessionLocal
from app.db.models.ubigeo_estado import UbigeoEstado


def registrar_ubigeo_estado(ubigeo_estado):
    db = SessionLocal()
    try:
        db_ubigeo_estado = UbigeoEstado(
            Id_Ubigeo = ubigeo_estado.Id_Ubigeo,
            Estado = ubigeo_estado.Estado
        )

        db.add(db_ubigeo_estado)
        db.commit()
        db.refresh(db_ubigeo_estado)

        return db_ubigeo_estado
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al registrar el ubigeo_estado: " + str(e))
        
    finally:
        db.close()


def obtener_ubigeo_estado(id_UbigeoEstado: int):
    db = SessionLocal()
    try:
        db_ubigeo_estado =db.query(UbigeoEstado).filter(UbigeoEstado.Id_UbigeoEstado == id_UbigeoEstado).first()
        if db_ubigeo_estado is None:
            raise HTTPException(status_code=404, detail="UbigeoEstado no encontrado")
        
        return db_ubigeo_estado 
    except HTTPException as e:
        raise HTTPException(status_code= 500, detail="Error al obtener el ubigeo_estado: " + str(e.detail))
    finally:
        db.close()



def actualizar_ubigeo_estado(id_UbigeoEstado: int, ubigeo_estado):
    db = SessionLocal()
    try:
        db_ubigeo_estado = db.query(UbigeoEstado).filter(UbigeoEstado.Id_UbigeoEstado == id_UbigeoEstado).first()
        if db_ubigeo_estado is None:
            raise HTTPException(status_code=404, detail="UbigeoEstado no encontrado")
        db_ubigeo_estado.Id_Ubigeo = ubigeo_estado.Id_Ubigeo
        db_ubigeo_estado.Estado = ubigeo_estado.Estado

        db.commit()
        db.refresh(db_ubigeo_estado)    

        return db_ubigeo_estado
    
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al actualizar el ubigeo_estado: " + str(e.detail))

    finally:
        db.close()