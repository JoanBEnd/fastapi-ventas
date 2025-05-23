from app.db.conect import SessionLocal
from sqlalchemy import text
from app.db.models.cliente import Cliente
from fastapi import HTTPException   


def obtener_cliente(Id_Cliente: int):
    """
    Función para obtener un cliente por su ID.
    """
    # Crear una sesión de base de datos
    db = SessionLocal()
    
    try:                      
        query = text("SELECT Nombre, Apellido, Genero, Edad FROM Cliente WHERE id_Cliente = :Id_Cliente")
        result = db.execute(query, {"Id_Cliente": Id_Cliente})
        result = result.fetchone()  # Obtiene una sola fila del resultado        
        result = result._mapping  # Convierte el resultado a un diccionario        
        if result:            
            return result
            #return dict(result._mapping)  # Convierte el resultado a un diccionario
        else:
            return HTTPException(status_code=404, detail="No se encontró el cliente con el ID proporcionado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el cliente: {str(e)}")
    
    finally:
        db.close()  # Asegúrate de cerrar la sesión después de usarla

def registrar_cliente(cliente):
    db = SessionLocal()
    try:
        #Id_Cliente = db.query(Cliente).count() + 1
        
        db_cliente = Cliente(
          #  Id_Cliente=Id_Cliente,
            Nombre=cliente.Nombre,
            Apellido = cliente.Apellido,
            Genero = cliente.Genero,
            Edad = cliente.Edad
        )
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar el cliente: {str(e)}")
    finally:
        db.close()

def actualizar_cliente(Id_Cliente: int, cliente):
    db = SessionLocal()
    try:
        db_cliente = db.query(Cliente).filter(Cliente.Id_Cliente == Id_Cliente).first()
        if not db_cliente:
            return HTTPException(status_code=404, detail="No se encontró el cliente con el ID proporcionado")
        db_cliente.Nombre = cliente.Nombre
        db_cliente.Apellido = cliente.Apellido
        db_cliente.Genero = cliente.Genero
        db_cliente.Edad = cliente.Edad
        db.commit()
        db.refresh(db_cliente)
        
        return db_cliente
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")
    finally:
        db.close() 
 