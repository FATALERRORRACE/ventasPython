from database.db import Db

# the objective of this migration is created the left tables in the database ventas
class MigrateNewTables:
    def __init__(self):
        db = Db()
        # create table metodo_pago
        db.query(
            '''
            CREATE TABLE IF NOT EXISTS metodo_pago (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                activo BOOLEAN DEFAULT 1
            )
            '''
        )
        # create table  vendedor_responsable
        db.query(
            '''
            CREATE TABLE IF NOT EXISTS vendedor_responsable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                activo BOOLEAN DEFAULT 1
            )
        ''')
        
        # create table producto_precio
        db.query(
            '''
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo_producto CHAR(10) NOT NULL UNIQUE,
                activo BOOLEAN DEFAULT 1
            )
            '''
        )

        # clean records before run script
        print("Limpieza de datos en progreso...")
        db.query('DELETE FROM clientes;')
        db.query('DELETE FROM ventas;')
        db.query('DELETE FROM detalle_ventas;')
        db.query('DELETE FROM producto;')
        db.query('DELETE FROM metodo_pago;')
        db.query('DELETE FROM vendedor_responsable;')