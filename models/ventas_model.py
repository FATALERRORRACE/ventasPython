from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, DateTime, Numeric, Text, ForeignKey, func
)

Base = declarative_base()
class VentaModel(Base):
    __tablename__ = 'ventas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_factura = Column(String(50), unique=True, nullable=False)
    fecha_venta = Column(DateTime, nullable=False)
    cliente_id = Column(Integer)
    subtotal = Column(Numeric(12, 2))
    descuento_total = Column(Numeric(12, 2))
    total_venta = Column(Numeric(12, 2))
    metodo_pago_id = Column(Integer)
    vendedor_id = Column(Integer)
    observaciones = Column(Text)
    estado = Column(String(20), default='Completada')
    fecha_creacion = Column(DateTime, server_default=func.current_timestamp())