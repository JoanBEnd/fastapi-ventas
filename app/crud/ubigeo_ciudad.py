from app.db.conect import SessionLocal
from fastapi import HTTPException
from app.db.models.ubigeo_ciudad import UbigeoCiudad

def registrar_ubigeo_ciudad(ubigeo_ciudad): 
    db = SessionLocal()

    try:
        db_ubigeo_ciudad = UbigeoCiudad(
            Id_UbigeoEstado = ubigeo_ciudad.Id_UbigeoEstado,
            Ciudad = ubigeo_ciudad.Ciudad,
            Latitud = ubigeo_ciudad.Latitud,
            Longitud = ubigeo_ciudad.Longitud
        )

        db.add(db_ubigeo_ciudad)
        db.commit()   
        db.refresh(db_ubigeo_ciudad)

        return db_ubigeo_ciudad
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al registrar el ubigeo_ciudad: " + str(e))

    finally:
        db.close()


def obtener_ubigeo_ciudad(id_UbigeoCiudad: int):
    db = SessionLocal()

    try:    
        db_ubigeo_ciudad= db.query(UbigeoCiudad).filter(UbigeoCiudad.Id_UbigeoCiudad == id_UbigeoCiudad).first()
        if db_ubigeo_ciudad is None:
            raise HTTPException(status_code=404, detail="UbigeoCiudad no encontrado")   
        
        return db_ubigeo_ciudad
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al obtener el ubigeo_ciudad: " + str(e.detail))
    finally:
        db.close()


def actualizar_ubigeo_ciudad(id_UbigeoCiudad: int, ubigeo_ciudad):  
    db = SessionLocal()

    try:
        db_ubigeo_ciudad = db.query(UbigeoCiudad).filter(UbigeoCiudad.Id_UbigeoCiudad == id_UbigeoCiudad).first()
        if db_ubigeo_ciudad is None:
            raise HTTPException(status_code=404, detail="UbigeoCiudad no encontrado.")
        db_ubigeo_ciudad.Id_UbigeoEstado = ubigeo_ciudad.Id_UbigeoEstado
        db_ubigeo_ciudad.Ciudad = ubigeo_ciudad.Ciudad
        db_ubigeo_ciudad.Latitud = ubigeo_ciudad.Latitud
        db_ubigeo_ciudad.Longitud = ubigeo_ciudad.Longitud

        db.commit()
        db.refresh(db_ubigeo_ciudad)

        return db_ubigeo_ciudad
    
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al actualizar el UbigeoCiudad " + str(e.detail))
    finally:
        db.close()
        