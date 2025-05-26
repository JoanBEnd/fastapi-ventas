from app.db.conect import SessionLocal
from app.db.models.categoria import Categoria
from fastapi import HTTPException

def registrar_categoria(categoria):
    db = SessionLocal()

    try:
        #Id_Categoria = db.query(Categoria).count() + 1
        db_categoria = Categoria(
         #   Id_Categoria = Id_Categoria,
            Categoria = categoria.Categoria
        )

        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria
    except Exception as e:
        raise HTTPException(status_code = 404, detail = f"Error al registrar la categoria: {str(e)}")
    
    finally:
        db.close()


def obtener_categoria(id_Categoria: int):
    db = SessionLocal()
    try:
        db_categoria = db.query(Categoria).filter(Categoria.id_Categoria == id_Categoria).first()
        if not db_categoria:
           raise HTTPException(status_code=404, detail="No se encontró la categoria con el ID proporcionado")         
        
        return db_categoria
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")
    finally:
        db.close()


def actualizar_categoria(Id_Categoria: int, categoria):
    db = SessionLocal()
    try:
        db_categoria = db.query(Categoria).filter(Categoria.id_Categoria == Id_Categoria).first()
        if not db_categoria:
            raise HTTPException(status_code= 404, detail="No se encontrò la categoria con el Id proporcionado")
        
        db_categoria.Categoria = categoria.Categoria
        db.commit()
        db.refresh(db_categoria)        
        return db_categoria
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")  
    
    finally:
        db.close()

def obtener_ultimo_registro():
    db = SessionLocal()
    print("holaaaaa")
    try:
        db_ultimo_registro = db.query(Categoria).order_by(Categoria.id_Categoria.desc()).first()
        if not db_ultimo_registro:
           raise HTTPException(status_code=404, detail="No se encontró la categoria con el ID proporcionado")         
        return db_ultimo_registro
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al querer obtener el valor:  {str(e)}")
    finally:
        db.close()