from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL
from app.db.conect import Base

class venta_detalle(Base):
    __tablename__ = "venta_detalle"
    Id_VentaDetalle = Column(Integer, primary_key=True, nullable= False, autoincrement=True)
    Transaccion_ID = Column(Integer, ForeignKey("venta.Transaccion_ID"), nullable=False)
    Id_Producto =  Column(Integer, ForeignKey("Producto.Id_Producto"), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Precio_Unitario = Column(DECIMAL(10), nullable= False)
    Total = Column(DECIMAL(10, 2), nullable=False)

