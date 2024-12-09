from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.connection import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    anio_publicacion = Column(Integer, nullable=False)
    tipo = Column(Enum("Libro", "Revista"), nullable=False)

    __mapper_args__ = {
    "polymorphic_identity": "item",
    "polymorphic_on": tipo,  # Determina qué clase hija corresponde
    }


class Libro(Item):
    __tablename__ = "libros"

    id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    autor = Column(String(255), nullable=False)  # Obligatorio para libros

    __mapper_args__ = {
        "polymorphic_identity": "Libro",  # Identidad única para este tipo
    }

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo={self.titulo}, autor={self.autor}, anio_publicacion={self.anio_publicacion})>"
    

class Revista(Item):
    __tablename__ = "revistas"

    id = Column(Integer, ForeignKey("items.id"), primary_key=True)
    edicion = Column(String(50), nullable=False)  # Obligatorio para revistas

    __mapper_args__ = {
        "polymorphic_identity": "Revista",  # Identidad única para este tipo
    }

    def __repr__(self):
        return f"<Revista(id={self.id}, titulo={self.titulo}, edicion={self.edicion}, anio_publicacion={self.anio_publicacion})>"
    

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_item = Column(Integer, ForeignKey("items.id"), nullable=True)
    fecha_prestamo = Column(String(10), nullable=False) #DD-MM-YYYY
    devuelto = Column(Boolean, default=False)

    item = relationship("Item", backref="prestamos")

    def __repr__(self):
        estado = "Devuelto" if self.devuelto else "No devuelto"
        return f"<Prestamo(id={self.id}, id_item={self.id_item}, estado={estado})>"
