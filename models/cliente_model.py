from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ClienteModel(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rut = Column(String(20), nullable=False)
    nombre = Column(String(200), nullable=False)
    activo = Column(Boolean, nullable=True, default=True)