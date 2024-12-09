from database.connection import Database
from app.biblioteca_service import BibliotecaService
from app.models import Item, Libro, Revista

def main():
    db = Database(user="user", password="password", host="localhost", database="bibliotecaFastApi")
    db.crear_tablas()
    session = db.obtener_sesion()
    biblioteca_service = BibliotecaService(session)

    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar Libro")
        print("2. Agregar Revista")
        print("3. Listar Items")
        print("4. Prestar Item")
        print("5. Eliminar item por ID")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            anio = int(input("Año de publicación: "))
            autor = input("Autor del libro: ")
            libro = Libro(titulo=titulo, anio_publicacion=anio, tipo="Libro", autor=autor)
            biblioteca_service.agregar_item(libro)

        elif opcion == "2":
            titulo = input("Título de la revista: ")
            anio = int(input("Año de publicación: "))
            edicion = input("Edición de la revista: ")
            revista = Revista(titulo=titulo, anio_publicacion=anio, tipo="Revista", edicion=edicion)
            biblioteca_service.agregar_item(revista)

        elif opcion == "3":
            biblioteca_service.listar_items()

        elif opcion == "4":
            id_item = int(input("ID del item a prestar: "))
            fecha = input("Fecha del préstamo (DD-MM-YYYY): ")
            biblioteca_service.prestar_item(id_item, fecha)
        
        elif opcion == "5":
            id_item = int(input("ID del item a eliminar: "))
            biblioteca_service.eliminar_item(id_item)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
