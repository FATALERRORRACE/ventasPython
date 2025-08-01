import pandas as pd
from repositories.cliente_repository import ClienteRepository
from repositories.ventas_repository import VentasRepository
from repositories.metodo_pago_repository import MetodoPagoRepository
from repositories.vendedor_responsable_repository import VendedorResponsableRepository
from repositories.producto_repository import ProductoRepository
from repositories.detalle_venta_repository import DetalleVentaRepository
import time

class ExcelProcessor:
    def __init__(self, path = '', sheetName = 'Sheet1'): 
        # if not hasattr(self, 'metodoPagoRepository'): recordar validar cada atributo antes de inicializarlo 
        # if not hasattr(self, 'vendedorResponsableRepository'):  recordar validar cada atributo antes de inicializarlo
        self.clienteRepository = ClienteRepository() # Initialize repository for clientes
        self.ventasRepository = VentasRepository() # Initialize repository for ventas
        self.metodoPagoRepository = MetodoPagoRepository() # Initialize repository for clientes
        self.vendedorResponsableRepository = VendedorResponsableRepository() # Initialize repository for ventas
        self.productoRepository = ProductoRepository()
        self.detalleVentaRepository = DetalleVentaRepository()
        self.clientesInfo = {} # Dictionary with the clientes created during the execution
        self.productoInfo = {}
        self.ventasInfo = {} # Dictionary with the ventas created during the execution
        self.metodoPagoInfo = {} # Dictionary with the clientes created during the execution
        self.vendedorInfo = {} # Dictionary with the ventas created during the execution
        self.path = path
        self.sheetName = sheetName
        self.excel_reader = pd.read_excel(self.path, sheet_name = self.sheetName)

    def getData(self):
        if self.excel_reader.empty:
            print("No data found in the Excel file.")
            return
        counter = 0
        for row in self.excel_reader.itertuples(index=True):
            if not str(row.rut_cliente)[-1].isdigit():
                print(f"Fila excluida por rut inválido: {row.rut_cliente}")
                continue
            counter+=1

            ## funciones que procesan los datos
            self.calcularTotales(row)
            self.validarProducto(row)
            self.validarMetodoPago(row)
            self.validarVendedor(row)
            self.validarCliente(row)
            self.validarVenta(row)
            self.validarDetalleVenta(row)
            # fin

        print(f"{counter} filas procesadas.")

        self.mostrarTopValores()

        print("Gracias 😀😀")

    def validarCliente(self, row):
        if row.rut_cliente not in self.clientesInfo:
            userCreated = self.clienteRepository.crear(
                rut=row.rut_cliente,
                nombre=row.nombre_cliente, 
                activo=True
            )
            self.clientesInfo[row.rut_cliente] = userCreated.lastrowid

    def validarVenta(self, row):
        ventaCreated = self.ventasRepository.crear(
            numero_factura = row.numero_factura,
            fecha_venta = row.fecha_venta,
            cliente_id = self.clientesInfo[row.rut_cliente],
            subtotal = self.subtotal_linea,
            descuento_total = self.descuento_total,
            total_venta = self.subtotal_linea - self.descuento_total,
            metodo_pago_id = self.metodoPagoInfo[row.metodo_pago],
            vendedor_id = self.vendedorInfo[row.vendedor_responsable],
            observaciones = row.observaciones,
            estado = row.estado_venta,
            fecha_creacion = pd.Timestamp.today().strftime('%Y-%m-%d %H:%M:%S')
        )
        if row.numero_factura not in self.ventasInfo:
            self.ventasInfo[row.numero_factura] = ventaCreated.lastrowid
            

    def calcularTotales(self, row):
        # encontré una diferencia en los requerimientos, especificaré esto en la reunión que tengamos el viernes referente al subtotal y total
        self.precio_unitario_to_float = 0
        self.subtotal_linea = 0
        self.descuento_total = 0
        precio_unitario = row.precio_unitario.replace('$', '').replace(',', '')
        try:
            self.precio_unitario_to_float = float(precio_unitario)
            # cálculo inicial self.subtotal_linea = row.cantidad_vendida * self.precio_unitario_to_float * (1 - row.descuento_porcentaje/100) 
            self.subtotal_linea = row.cantidad_vendida * self.precio_unitario_to_float # cantidad_vendida * precio_unitario 
            self.descuento_total = row.cantidad_vendida * self.precio_unitario_to_float * (row.descuento_porcentaje/100)
        except ValueError:
            print(f"Error convirtiendo precio_unitario'{row.precio_unitario}' a decimal. se guarda en cero.")


    def validarMetodoPago(self, row):
        metodo_pago = row.metodo_pago
        if metodo_pago not in self.metodoPagoInfo:
            creado = self.metodoPagoRepository.crear(nombre=metodo_pago)
            self.metodoPagoInfo[metodo_pago] = creado.lastrowid

    def validarVendedor(self, row):
        vendedor = row.vendedor_responsable
        if vendedor not in self.vendedorInfo:
            creado = self.vendedorResponsableRepository.crear(nombre=vendedor)
            self.vendedorInfo[vendedor] = creado.lastrowid

    def validarProducto(self, row):
        codigo_producto = row.codigo_producto
        if codigo_producto not in self.productoInfo:
            creado = self.productoRepository.crear(
                codigo_producto=codigo_producto
            )
            self.productoInfo[codigo_producto] = creado.lastrowid

    def validarDetalleVenta(self, row):
        self.detalleVentaRepository.crear(
            venta_id=self.ventasInfo.get(row.numero_factura),
            producto_id=self.productoInfo.get(row.codigo_producto),
            cantidad=row.cantidad_vendida,
            precio_unitario=self.precio_unitario_to_float,
            descuento_porcentaje=row.descuento_porcentaje,
            subtotal_linea=self.subtotal_linea
        )

    def mostrarTopValores(self):
        top_data = self.ventasRepository.topDiez()
        print("💵 El top 10 de clientes que más han comprado en los 6 meses:")
        for index, venta in enumerate(top_data, 1):
            time.sleep(.5)
            print(f"{index}. {venta}")
        top_data = self.ventasRepository.topDiezVendidos()
        print("💵 El top 10 de los productos más vendidos en todo el histórico:")
        for index, venta in enumerate(top_data, 1):
            time.sleep(.5)
            print(f"{index}. {venta}")
        top_data = self.ventasRepository.ventasDosMeses150mil()
        print("💵 Todas las ventas completadas de los últimos 2 meses con valor mayor a $150.000:")
        for index, venta in enumerate(top_data, 1):
            time.sleep(.2)
            print(f"{index}. {venta}")