# app/crud.py

from sqlalchemy.orm import Session
from . import schemas, models


def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.ProductosDB(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def consultar_productos(db: Session,start: int = 0, limit: int = 10):
    return db.query(models.ProductosDB).offset(start).limit(limit).all()
