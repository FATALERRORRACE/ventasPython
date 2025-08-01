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
        )

        # Check if the venta already exists by numero_factura
        existing = self.db.query(
            "SELECT COUNT(*) FROM ventas WHERE numero_factura = ?",
            (self.venta.numero_factura,)
        )

        if existing and isinstance(existing, list) and existing[0][0] > 0:
            # Update existing venta
            return self.db.query(
                "UPDATE ventas SET subtotal=subtotal+?, descuento_total=descuento_total+?, total_venta=total_venta+?, observaciones=TRIM(observaciones || ' - ' || ?) WHERE numero_factura=?",
                (
                    self.venta.subtotal,
                    self.venta.descuento_total,
                    self.venta.total_venta,
                    self.venta.observaciones,
                    self.venta.numero_factura
                )
            )
        else:
            # Insert new venta
            return self.db.query(
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
        
    def topDiez(self):
        query = """
            SELECT c.id, c.nombre, SUM(v.total_venta) AS total_ventas, COUNT(v.id) AS numero_ventas
            FROM ventas v
            JOIN clientes c ON v.cliente_id = c.id
            WHERE v.estado = 'Completada'
                AND v.fecha_venta >= DATE('now', '-6 months')
            GROUP BY c.id, c.nombre
            ORDER BY total_ventas DESC
            LIMIT 10
        """
        return self.db.query(query)

    def topDiezVendidos(self):
        query = """
            SELECT p.id, p.codigo_producto, SUM(vd.cantidad) AS total_unidades, SUM(vd.cantidad * vd.precio_unitario) AS total_ventas
            FROM detalle_ventas vd
            JOIN producto p ON vd.producto_id = p.id
            GROUP BY p.id, p.codigo_producto
            ORDER BY total_unidades DESC
            LIMIT 10
        """
        return self.db.query(query)

    def ventasDosMeses150mil(self):
        query = """
            SELECT *
            FROM ventas
            WHERE estado = 'Completada'
                AND fecha_venta >= DATE('now', '-2 months')
                AND total_venta > 150000
        """
        return self.db.query(query)