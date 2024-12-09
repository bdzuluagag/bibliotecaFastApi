from sqlalchemy.orm import Session
from app.models import Item, Prestamo

class BibliotecaService:

    def __init__(self, db_session: Session):
        self.session = db_session


    def agregar_item(self, item):
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item


    def listar_items(self):
        items = self.session.query(Item).all()
        resultado = []
        for item in items:
            prestamo_activo = self.session.query(Prestamo).filter(Prestamo.id_item == item.id, Prestamo.devuelto == False).first()

            if prestamo_activo:
                estado = "Prestado"
            else:
                estado = "Disponible"

            resultado.append({
                "id": item.id,
                "titulo": item.titulo,
                "anio_publicacion": item.anio_publicacion,
                "tipo": item.tipo,
                "estado": estado
            })

            return resultado


    def prestar_item(self, id_item, fecha_prestamo):
        prestamo_activo = self.session.query(Prestamo).filter(Prestamo.id_item == id_item, Prestamo.devuelto == False).first()

        if prestamo_activo:
            return {"error": "Item ya está prestado."}

        prestamo = Prestamo(id_item=id_item, fecha_prestamo=fecha_prestamo)
        self.session.add(prestamo)
        self.session.commit()
        self.session.refresh(prestamo)
        return {"message": "Item prestado correctamente"}


    def devolver_item(self, id_item):
        prestamo = self.session.query(Prestamo).filter(Prestamo.id_item == id_item, Prestamo.devuelto == False).first()

        if prestamo:
            prestamo.devuelto = True
            self.session.commit()
            return {"message": "Item devuelto correctamente"}
        else:
            return {"message": f"No se encontró ningun préstamo activo item con ID {id_item}"}


    def eliminar_item(self, id_item):
        item = self.session.query(Item).get(id_item)

        if item:
            self.session.delete(item)
            self.session.commit()
            print(f"Item con ID {id_item} eliminado correctamente.")
        else:
            return {"message": f"No se encontró ningun item con ID {id_item}."}


    def listar_prestamos(self):
        prestamos = self.session.query(Prestamo).all()
        resultado = []
        for prestamo in prestamos:
            resultado.append({
                "id": prestamo.id,
                "id_item": prestamo.id_item,
                "fecha_prestamo": prestamo.fecha_prestamo,
                "devuelto": prestamo.devuelto,
            })
        return resultado


    

