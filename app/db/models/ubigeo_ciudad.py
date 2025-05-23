from app.db.conect import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class UbigeoCiudad(Base):
    __tablename__ = "UbigeoCiudad"
    Id_UbigeoCiudad = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Id_UbigeoEstado = Column(Integer, ForeignKey("UbigeoEstado.Id_UbigeoEstado"))
    Ciudad = Column(String(100), nullable=False)
    Latitud = Column(Float, nullable=False)
    Longitud = Column(Float, nullable=False)
