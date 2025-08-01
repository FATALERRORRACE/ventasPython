from database.db import Db

class ProductoRepository:
    def __init__(self):
        self.db = Db()

    def crear(self, codigo_producto):
        return self.db.query(
            "INSERT INTO producto (codigo_producto) VALUES (?)",
            (codigo_producto,)
        )
