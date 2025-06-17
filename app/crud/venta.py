from app.db.conect import SessionLocal
from app.db.models.venta import venta
from fastapi import HTTPException
from sqlalchemy import text


def registrar_venta(venta_):
    db = SessionLocal()
    try:
        db_venta = venta(
            Id_Cliente = venta_.Id_Cliente,
            Id_Empleado = venta_.Id_Empleado,
            Id_UbigeoCiudad = venta_.Id_UbigeoCiudad,
            Venta_Total = venta_.Venta_Total,
            fecha_registro = venta_.fecha_registro
        )
        db.add(db_venta)
        db.commit()
        db.refresh(db_venta)
        return db_venta

    finally:
        db.close()

def obtener_venta(Transaccion_ID: int):
    db = SessionLocal()

    try:

        db_venta = db.query(venta).filter(venta.Transaccion_ID == Transaccion_ID).first()
        if db_venta is None:
            raise HTTPException(status_code=404, detail="No se encontró la venta")
        return db_venta
    
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al obtener la información de la venta" + str(e.detail))

    finally:
        db.close()

def actualizar_venta(Transaccion_ID: int, venta_):
    db = SessionLocal()
    try:
        db_venta = db.query(venta).filter(venta.Transaccion_ID == Transaccion_ID).first()
        if db_venta is None:
            raise HTTPException(status_code=404, detail="No se encontró la venta")
        db_venta.Id_Cliente = venta_.Id_Cliente
        db_venta.Id_Empleado = venta_.Id_Empleado
        db_venta.Id_UbigeoCiudad = db_venta.Id_UbigeoCiudad
        db_venta.Venta_Total = venta_.Venta_Total
        db_venta.fecha_registro = venta_.fecha_registro

        db.commit()
        db.refresh(db_venta)
        return db_venta
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al actualizar la venta")
    finally:
        db.close()


def obtener_ultima_venta():
    db = SessionLocal()

    try:
        db_venta = db.query(venta).order_by(venta.Transaccion_ID.desc()).first()
        if db_venta is None:
            raise HTTPException(status_code=404, detail="No se encontró ninguna venta registrada")
        return db_venta
    
    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Error al obtener la última venta: " + str(e.detail))
    finally:
        db.close()

        # query = text("exec sp_Registrar_Venta_Aleatoria :Id_Cliente, :Id_Empleado, :Id_Producto,  :fecha_registro")
        # db_venta = db.execute(query, {
        #     "Id_Cliente": venta_.Id_Cliente,
        #     "Id_Empleado": venta_.Id_Empleado,
        #     "Id_Producto": venta_.Id_Producto,
        #     "fecha_registro": venta_.fecha_registro
        # })

def registrar_venta_aleatoria(venta_):
    db = SessionLocal()
    try:
        # Accede al cursor nativo de pyodbc
        conn = db.connection()
        raw_conn = conn.connection
        cursor = raw_conn.cursor()

        # Ejecuta el procedimiento con parámetros posicionales
        cursor.execute(
            "EXEC sp_Registrar_Venta_Aleatoria ?, ?, ?, ?",
            venta_.Id_Cliente,
            venta_.Id_Empleado,
            venta_.Id_Producto,
            venta_.fecha_registro
        )

        # Avanza hasta encontrar un result set válido
        result = None
        while True:
            if cursor.description:  # Encontró un result set con columnas
                result = cursor.fetchone()
                break
            if not cursor.nextset():  # No hay más result sets
                break

        if result is None:
            raise HTTPException(status_code=500, detail="El procedimiento no devolvió ningún resultado")

        db.commit()

        # Devuelve el resultado como dict
        return dict(zip([col[0] for col in cursor.description], result))

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al registrar la venta aleatoria: {str(e)}")
    finally:
        db.close()

