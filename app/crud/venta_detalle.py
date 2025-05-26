from app.crud import venta
from app.db.conect import SessionLocal
from app.db.models.venta_detalle import venta_detalle
from fastapi import HTTPException


def registrar_venta_detalle(ventaDetalle):
    db = SessionLocal()
    try:
        db_venta_detalle = venta_detalle(
            Transaccion_ID= ventaDetalle.TransaccionID,
            Id_Producto = ventaDetalle.Id_Producto,
            Cantidad = ventaDetalle.Cantidad,
            Precio_Unitario = ventaDetalle.Precio_Unitario,
            Total = ventaDetalle.Total
        )

        db.add(db_venta_detalle)
        db.commit()
        db.refresh(db_venta_detalle)

        return db_venta_detalle
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="No se pudo realizar el registro de la venta detalle" + str(e))
    
    finally:
        db.close()


def obtener_venta_detalle(Transaccion_ID: int):
    db = SessionLocal()

    try:
        db_venta_detalle = db.query(venta_detalle).filter(venta_detalle.Transaccion_ID == Transaccion_ID).first()
        if db_venta_detalle is None:
            raise HTTPException(status_code=404, detail="No se encontró ningun detalle de la transacción" )

        return db_venta_detalle

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al obtener el detalle " + str(e))

    finally:

        db.close()


def actualizar_venta_detalle(Transaccion_ID:int, ventaDetalle):
    db = SessionLocal()

    try:
        db_venta_detalle = db.query(venta_detalle).filter(venta_detalle.Transaccion_ID == Transaccion_ID).first()
        if db_venta_detalle is None:
            raise HTTPException(status_code=404, detail="No se encontró ningun detalle de la transacción" )
        db_venta_detalle.Cantidad = ventaDetalle.Cantidad
        db_venta_detalle.Precio_Unitario = ventaDetalle.Precio_Unitario
        db_venta_detalle.Total = ventaDetalle.Total

        db.commit()
        db.refresh(db_venta_detalle)
        return db_venta_detalle
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al actualizar el detalle de la venta "+ str(e) )
    finally:
        db.close()