from app.db.conect  import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DATETIME

class venta(Base):

    __tablename__ = "venta"
    Transaccion_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Id_Cliente = Column(Integer, ForeignKey("Cliente.Id_Cliente"), nullable=False   )
    Id_Empleado = Column(Integer, ForeignKey("Empleado.Id_Empleado"), nullable=False)
    Id_UbigeoCiudad = Column(Integer, ForeignKey("UbigeoCiudad.Id_UbigeoCiudad"), nullable=False)
    Venta_Total = Column(Float, nullable=False)
    fecha_registro = Column(DATETIME, nullable=False)