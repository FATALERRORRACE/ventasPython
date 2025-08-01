from database.db import Db
from models.metodo_pago_model import MetodoPagoModel

class MetodoPagoRepository:
    def __init__(self):
        self.db = Db()

    def crear(self, nombre, activo=True):
        #agregar MODELO
        return self.db.query(
            "INSERT INTO metodo_pago (nombre, activo) VALUES (?, ?)",
            (nombre, activo)
        )
