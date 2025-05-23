from app.db.conect import SessionLocal
from fastapi import HTTPException
from app.db.models.usuarios import Usuarios

def registrar_usuario(usuario):
    db = SessionLocal()
    try:
        
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()