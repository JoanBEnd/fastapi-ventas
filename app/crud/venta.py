from app.db.conect import SessionLocal
from app.db.models.venta import venta
from fastapi import HTTPException


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