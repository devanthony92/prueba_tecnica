
# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, models, schemas, crud

app = FastAPI()

@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/productos/", response_model=schemas.Producto)
def create_product(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.Producto])
def  list_products(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.consultar_productos(db,skip=skip,limit=limit)

@app.get("/productos/{id}",response_model=schemas.Producto)
def find_product(id_producto : int,  db: Session = Depends(database.get_db)):
    return crud.ver_producto(db,id_producto)


@app.patch("/productos/{id}",response_model=schemas.ProductoUpdate)
def update_product(id_producto : int, data: schemas.ProductoUpdate, db: Session = Depends(database.get_db)):
    return crud.actualizar_producto(db,id_producto,data)

@app.delete("/productos/{id}")
def delete_product(id_producto : int,  db: Session = Depends(database.get_db)):
    return crud.eliminar_producto(id_producto,db)