from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    titulo: str
    anio_publicacion: int
    tipo: str


class LibroCreate(ItemBase):
    autor: str


class RevistaCreate(ItemBase):
    edicion: str


class PrestamoBase(BaseModel):
    fecha_prestamo: str
    devuelto: Optional[bool] = False


class PrestamoCreate(PrestamoBase):
    id_item: int