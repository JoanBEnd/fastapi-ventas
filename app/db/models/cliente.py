from sqlalchemy import Column, Integer, String
from app.db.conect import Base

class Cliente(Base):
    __tablename__ = "Cliente"
    Id_Cliente = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    Nombre = Column(String(50), nullable=False)
    Apellido = Column(String(50), nullable=False)
    Genero = Column(String(10), nullable=False)
    Edad = Column(Integer, nullable=False)

#from pydantic import BaseModel  
#class Cliente(BaseModel):
#    Nombre: str
#    Apellido: str
#    Genero: str
#    Edad: int   