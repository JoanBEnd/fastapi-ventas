from app.db.conect import Base
from sqlalchemy import Column, Integer, String, Float, DECIMAL, ForeignKey


class Producto(Base):
    __tablename__ = "Producto"

    Id_Producto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Id_Categoria = Column(Integer, ForeignKey("Categoria.id_Categoria"), nullable=False)
    Producto = Column(String(180), nullable=False)
    Precio_Actual = Column(DECIMAL(10, 2), nullable=False)


    