from app.db.conect import SessionLocal
from fastapi import HTTPException
from app.db.models.ubigeo_region import UbigeoRegion


def registrar_ubigeo_region(ubigeo_region):
    db = SessionLocal()
    try:
        db_ubigeo_region = UbigeoRegion(         
            Region = ubigeo_region.Region
        )
        db.add(db_ubigeo_region)
        db.commit()
        db.refresh(ubigeo_region)
        return ubigeo_region

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al registrar el ubigeo_region: " + str(e))
    
    finally:
        db.close()

def obtener_ubigeo_region(id_Ubigeo: int):
    db = SessionLocal()
    try:
        db_ubigeo_region = db.query(UbigeoRegion).filter(UbigeoRegion.Id_Ubigeo == id_Ubigeo).first()  
        if db_ubigeo_region is None:
            raise HTTPException(status_code=404, detail="UbigeoRegion no encontrado")
        
        return db_ubigeo_region
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail="Error al obtener el ubigeo_region: " + str(e.detail))

    finally:
        db.close()

def actualizar_ubigeo_region(id_Ubigeo: int, ubigeoRegion):
    db = SessionLocal()
    try:
        db_ubigeo_region = db.query(UbigeoRegion).filter(UbigeoRegion.Id_Ubigeo == id_Ubigeo).first()
        if db_ubigeo_region is None:
            raise HTTPException(status_code=404, detail="UbigeoRegion no encontrado")
        db_ubigeo_region.Region = ubigeoRegion.Region
        db.commit()
        db.refresh(db_ubigeo_region)
        return db_ubigeo_region
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al actualizar el ubigeo_region: " + str(e.detail))
    
    finally:
        db.close()
