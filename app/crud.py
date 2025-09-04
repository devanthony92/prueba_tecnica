# app/crud.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import schemas, models


def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.ProductosDB(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def consultar_productos(db: Session,skip: int = 0, limit: int = 10):
    return db.query(models.ProductosDB).offset(skip).limit(limit).all()

def ver_producto(db : Session, id_product : int):
    producto = db.query(models.ProductosDB).get(id_product)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


def actualizar_producto(db: Session,  id_producto :  int, datos_actualizados : schemas.ProductoUpdate):
    producto = db.query(models.ProductosDB).filter(models.ProductosDB.id == id_producto).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    datos_dict = datos_actualizados.dict(exclude_unset=True)

    for campo, valor in datos_dict.items():
        setattr(producto, campo, valor)

    db.commit()
    db.refresh(producto)

    return producto    

def eliminar_producto(id_producto : int, db : Session):
    try:
        producto = db.query(models.ProductosDB).filter(models.ProductosDB.id == id_producto).first()
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        db.delete(producto)
        db.commit()
        return {
            "detail": "Producto eliminado",
            "producto": schemas.Producto.model_validate(producto)
        }

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al eliminar el producto")

