from database.db import Db
from models.vendedor_responsable_model import VendedorResponsableModel

class VendedorResponsableRepository:
    def __init__(self):
        self.db = Db()

    def crear(self, nombre, activo=True):
        #agregar MODELO
        return self.db.query(
            "INSERT INTO vendedor_responsable (nombre, activo) VALUES (?, ?)",
            (nombre, activo)
        )