from app.db.conect import Base
from sqlalchemy import column, Integer, String, ForeignKey, VARBINARY, DATETIME


class Usuarios(Base):
    __tablename__= "Usuarios"
    
    Id_Empleado= column(Integer, ForeignKey("Empleado.Id_Empleado"))
    UserName = column(String(50), unique=True, index=True, nullable=False)
    Password = column(String(50), nullable=False)
    salt = column(VARBINARY(29), nullable=False)
    Fecha_Creacion = column(DATETIME, nullable=False)
