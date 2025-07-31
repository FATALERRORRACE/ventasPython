from database.db import Db
from models.ventas_model import VentaModel

class VentasRepository:
    def __init__(self):
        self.db = Db()
        self.venta = None

    def crear(self, numero_factura, fecha_venta, cliente_id, subtotal, descuento_total, total_venta, metodo_pago_id, vendedor_id, observaciones, estado, fecha_creacion):
        self.venta = VentaModel(
            numero_factura=numero_factura,
            fecha_venta=fecha_venta,
            cliente_id=cliente_id,
            subtotal=subtotal,
            descuento_total=descuento_total,
            total_venta=total_venta,
            metodo_pago_id=metodo_pago_id,
            vendedor_id=vendedor_id,
            observaciones=observaciones,
            estado=estado
            # fecha_creacion=fecha_creacion
        )

        self.db.query(
            "INSERT INTO ventas (numero_factura, fecha_venta, cliente_id, subtotal, descuento_total, total_venta, metodo_pago_id, vendedor_id, observaciones, estado, fecha_creacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                self.venta.numero_factura,
                self.venta.fecha_venta,
                self.venta.cliente_id,
                self.venta.subtotal,
                self.venta.descuento_total,
                self.venta.total_venta,
                self.venta.metodo_pago_id,
                self.venta.vendedor_id,
                self.venta.observaciones,
                self.venta.estado,
                self.venta.fecha_creacion
            )
        )