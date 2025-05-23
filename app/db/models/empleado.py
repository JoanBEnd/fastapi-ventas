from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.conect import Base

class Empleado(Base):
    __tablename__ = "Empleado"

    Id_Empleado = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    Nombre = Column(String(120), nullable=False)
    Apellido = Column(String(120), nullable=False)
    id_rol = Column(Integer, ForeignKey("roles.id_rol"), nullable=False)
    correo = Column(String(75), nullable=False)

