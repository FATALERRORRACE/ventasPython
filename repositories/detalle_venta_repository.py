from database.db import Db
from models.detalle_ventas_model import DetalleVentasModel

class DetalleVentaRepository:
    def __init__(self):
        self.db = Db()

    def crear(self, venta_id, producto_id, cantidad, precio_unitario, descuento_porcentaje=0, subtotal_linea=None):
        result = self.db.query(
            "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, descuento_porcentaje, subtotal_linea) VALUES (?, ?, ?, ?, ?, ?)",
            (venta_id, producto_id, cantidad, precio_unitario, descuento_porcentaje, subtotal_linea)
        )
        return result
