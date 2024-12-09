from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

Base = declarative_base()

class Database:
    def __init__(self, host, user, password, database):
        self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
        self.Session = sessionmaker(bind=self.engine)

    def crear_tablas(self):
        Base.metadata.create_all(self.engine)

    def obtener_sesion(self):
        session = self.Session
        try:
            yield session
        finally:
            session.close()
        