from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from biblioteca_service import BibliotecaService
from schemas import LibroCreate, RevistaCreate
import models

router = APIRouter()


@router.post("/items/libros/")
def agregar_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    servicio = BibliotecaService(db)
    nuevo_libro = models.Libro(
        titulo = libro.titulo,
        anio_publicacion = libro.anio_publicacion,
        autor = libro.autor,
    )
    return servicio.agregar_item(nuevo_libro)


@router.post("/items/revistas/")
def agregar_revista(revista: RevistaCreate, db: Session = Depends(get_db)):
    servicio = BibliotecaService(db)
    nueva_revista = models.Revista(
        titulo = revista.titulo,
        anio_publicacion = revista.anio_publicacion,
        edicion = revista.edicion,
    )
    return servicio.agregar_item(nueva_revista)


@router.get("/items/")
def listar_items(db: Session = Depends(get_db)):
    servicio = BibliotecaService(db)
    return servicio.listar_items()


@router.delete("/items/{id_item}")
def eliminar_item(id_item: int, db: Session = Depends(get_db)):
    servicio = BibliotecaService(db)
    return servicio.eliminar_item(id_item)
