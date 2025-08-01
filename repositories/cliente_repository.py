from database.db import Db
from models.cliente_model import ClienteModel

class ClienteRepository:
    def __init__(self):
        self.db = Db()
        self.cliente = None

    def crear(self, rut, nombre, activo):
        self.cliente = ClienteModel(
            rut=rut,
            nombre=nombre,
            activo=activo
        )
        return self.db.query(f"INSERT INTO {self.cliente.__tablename__} (rut, nombre, activo) VALUES (?, ?, ?)", (self.cliente.rut, self.cliente.nombre, self.cliente.activo))