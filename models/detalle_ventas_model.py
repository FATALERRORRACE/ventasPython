class DetalleVentasModel:
    def __init__(
        self,
        id=None,
        venta_id=None,
        producto_id=None,
        cantidad=None,
        precio_unitario=None,
        descuento_porcentaje=0,
        subtotal_linea=None
    ):
        self.id = id
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.descuento_porcentaje = descuento_porcentaje
        self.subtotal_linea = subtotal_linea