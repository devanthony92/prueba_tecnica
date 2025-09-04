
# app/main.py

from fastapi import FastAPI, Depends
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
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.Producto])
def  listar_productos(start: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.consultar_productos(db,start=start,limit=limit)