from app.db.conect import SessionLocal
from app.db.models.producto import Producto
from fastapi import HTTPException

def registrar_producto(producto):

    db = SessionLocal()
    try:
        #Id_Producto = db.query(Producto).count() + 1
        db_producto = Producto(
        #    Id_Producto = Id_Producto,
            Id_Categoria = producto.Id_Categoria,
            Producto = producto.Producto,
            Precio_Actual = producto.Precio_Actual
        )

        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar el producto: {str(e)}")
    
    finally:
        db.close()

def obtener_producto(Id_Producto: int):
    db = SessionLocal()
    try:
        db_producto = db.query(Producto).filter(Producto.Id_Producto == Id_Producto).first()
        if not db_producto:
            raise HTTPException(status_code=404, detail="No se encontró el producto con el ID proporcionado")        
        
        return db_producto
    
    finally:
        db.close()
    

def actualizar_producto(Id_Producto: int, producto):    
    db = SessionLocal()

    try:
        db_producto = db.query(Producto).filter(Producto.Id_Producto == Id_Producto).first()
        if not db_producto:
            raise HTTPException(status_code = 404, detail="No se encontrò el producto con el Id proporcionado")
        
        db_producto.Id_Categoria = producto.Id_Categoria
        db_producto.Producto = producto.Producto    
        db_producto.Precio_Actual = producto.Precio_Actual
        db.commit()
        db.refresh(db_producto)        
        return db_producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")   
    finally:
        db.close()

def obtener_ultimo_producto():
    db = SessionLocal()
    try:
        db_producto = db.query(Producto).order_by(Producto.Id_Producto.desc()).first()
        if not db_producto:
            raise HTTPException(status_code=404, detail="No se encontró ningún producto registrado")
        
        return db_producto
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el último producto: {str(e)}")
    finally:
        db.close()