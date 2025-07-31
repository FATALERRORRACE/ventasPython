import pandas as pd
from repositories.cliente_repository import ClienteRepository
from repositories.ventas_repository import VentasRepository

class ExcelProcessor:
    def __init__(self, path = '', sheetName = 'Sheet1'):
        self.clienteRepository = ClienteRepository() # Initialize repository for clientes
        self.ventasRepository = VentasRepository() # Initialize repository for ventas
        self.clientesInfo = {} # Dictionary with the clientes created during the execution
        self.ventasInfo = {} # Dictionary with the ventas created during the execution
        self.MetodoPagoInfo = {} # Dictionary with the clientes created during the execution
        self.VendedorInfo = {} # Dictionary with the ventas created during the execution
        self.path = path
        self.sheetName = sheetName
        self.excel_reader = pd.read_excel(self.path, sheet_name = self.sheetName)
    
    def getData(self):
        if self.excel_reader.empty:
            print("No data found in the Excel file.")
            return
        for row in self.excel_reader.itertuples(index=True):
            self.validarMetodoPago(row)
            self.validarVendedor(row)
            self.validarCliente(row)
            self.validarVenta(row)
            self.validarDetalleVenta(row)
            # INFO EXCEL:
            # numero_factura='FAC-2024-009741', 
            # fecha_venta='04/11/2024 11:40', 
            # rut_cliente='14.359.176-K', 
            # nombre_cliente='Yanet García Vergara', 
            # codigo_producto='PROD-006', 
            # cantidad_vendida=8, 
            # precio_unitario='$253,065.74', 
            # descuento_porcentaje=10.5, 
            # metodo_pago='Efectivo', 
            # vendedor_responsable='Laura Ruiz', 
            # observaciones=nan, 
            # estado_venta='Completada')
            print(f"Row {row.Index}: {row}")
            break

    def validarCliente(self, row):
        if self.clientesInfo[row.rut_cliente] == None:
            userCreated = self.clienteRepository.crear(
                rut=row.rut,
                nombre=row.nombre_cliente, 
                activo=True
            )
            self.clientesInfo[row.rut_cliente] = userCreated.lastrowid
            
    def validarVenta(self, row):
        if self.ventasInfo[row.numero_factura] == None:

            # numero_factura VARCHAR(50) UNIQUE NOT NULL,
            # fecha_venta TIMESTAMP NOT NULL,
            # cliente_id INTEGER,   
            # subtotal DECIMAL(12,2),
            # descuento_total DECIMAL(12,2),
            # total_venta DECIMAL(12,2),
            # metodo_pago_id INTEGER,
            # vendedor_id INTEGER,
            # observaciones TEXT,
            # estado VARCHAR(20) DEFAULT 'Completada', 
            # fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            userCreated = self.ventasRepository.crear(
                numero_factura = row.numero_factura
                fecha_venta = row.fecha_venta
                subtotal = row.
                cliente_id = self.clientesInfo[row.rut_cliente],
                observaciones = row.observaciones
                estado = row.estado_venta
                #fecha_creacion = row.fecha_venta
                )
            self.ventasInfo[row.numero_factura] = userCreated.lastrowid
    validarMetodoPago(
    validarVendedor(