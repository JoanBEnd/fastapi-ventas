from sqlalchemy import Column, Integer, String
from app.db.conect import Base

class roles(Base):
    __tablename__ ="roles"
    id_rol = Column(Integer, primary_key= True, index= True, autoincrement=True)    
    cargo = Column(String(100), nullable=False)
    