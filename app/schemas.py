# app/schemas.py

from pydantic import BaseModel, constr, condecimal,field_validator
from datetime import datetime
from typing import Optional

class Producto(BaseModel):
    id: int
    nombre: constr(min_length=1,max_length=100)
    descripcion: str | None = None
    precio: condecimal(max_digits=10, decimal_places=2)
    categoria: constr(max_length=50) | None = None
    created_at: datetime | None = None

    class Config:
        from_attributes = True # Esto permite convertir desde SQLAlchemy a Pydantic

class ProductoCreate(BaseModel):
    nombre: constr(min_length=1,max_length=100)
    descripcion: str | None = None
    precio: condecimal(max_digits=10, decimal_places=2)
    categoria: constr(max_length=50) | None = None

    @field_validator("precio")
    def validar_precio(cls, value):
        if value <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        return value

class ProductoUpdate(BaseModel):
    nombre: Optional[constr(min_length=1,max_length=100)] = None
    descripcion: Optional[str] = None
    precio: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    categoria: Optional[constr(max_length=50)] = None

    class Config:
        from_attributes = True # Esto permite convertir desde SQLAlchemy a Pydantic