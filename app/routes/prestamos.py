from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from biblioteca_service import BibliotecaService
from schemas import LibroCreate, RevistaCreate
import models

router = APIRouter()

@router.post("/prestamos/{id_item}/")
def prestar_item(id_item: int, fecha_prestamo: str, db: Session = Depends(get_db)):
    servicio = BibliotecaService(db)
    servicio.prestar_item(id_item, fecha_prestamo)


@router.put("/prestamos/devolver/")