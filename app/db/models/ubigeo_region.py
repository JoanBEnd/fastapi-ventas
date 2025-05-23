from sqlalchemy import Column, Integer, String
from app.db.conect import Base

class UbigeoRegion(Base):
    __tablename__ = "UbigeoRegion"
    Id_Ubigeo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Region = Column(String(100), nullable=False)    
    