# app/models.py

from sqlalchemy import func,Column,Integer,String,DECIMAL,TIMESTAMP
from .database import Base

class ProductosDB(Base):
    __tablename__ = "productos"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    nombre = Column(String(100),nullable=False)
    descripcion = Column(String(255))
    precio = Column(DECIMAL(10,2),nullable=False)
    categoria = Column(String(50))
    created_at = Column(TIMESTAMP,server_default=func.now())
