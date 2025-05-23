from app.db.conect import Base
from sqlalchemy import Column, Integer, String  , ForeignKey

class UbigeoEstado(Base):
    __tablename__ = "UbigeoEstado"
    Id_UbigeoEstado = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Id_Ubigeo = Column(Integer, ForeignKey("UbigeoRegion.Id_Ubigeo") , nullable=False)
    Estado = Column(String(100), nullable=False)
    
