from database.connection import Database

db = Database(
    host="localhost", 
    user="user", 
    password="password", 
    database="bibliotecaFastApi"
)

def get_db():
    with db.obtener_sesion() as session:
        yield session