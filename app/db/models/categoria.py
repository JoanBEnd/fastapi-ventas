
from app.db.conect import Base
from sqlalchemy import Column, Integer, String

class Categoria(Base):  
    __tablename__ = "Categoria"
    id_Categoria = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Categoria = Column(String(180), nullable=False)

