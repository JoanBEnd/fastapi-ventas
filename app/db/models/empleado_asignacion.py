from app.db.conect import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class EmpleadoAsignacion(Base):
    __tablename__ = "Empleado_Asginacion"

    id_Asignacion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_Empleado = Column(Integer, ForeignKey("Empleado.Id_Empleado"), nullable=False)
    id_UbigeoPermiso = Column(Integer, nullable=False)
    Ubigeo_Descripcion = Column(String(100), nullable=False)

