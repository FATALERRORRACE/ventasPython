import os
from services.excelProcessor_service import ExcelProcessor
class dataReader:
    def __init__(self):
        filePath = input("Ingrese la ruta de directorio del archivo: ")
        if os.path.exists(filePath) == False:
            #GENERAR LOOP DE RESPUESTAS
            print(f"El archivo '{filePath}' no existe.")
            return
        sheetName = input("Ingrese el nombre de la hoja a procesar, si dejas el campo vacío se usará \"Sheet1\" por defecto: ")
        #GENERAR LOOP DE RESPUESTAS AQUÍ TAMBIÉN
        excelProcessorInstance = ExcelProcessor(filePath, (sheetName if sheetName else "Sheet1"))
        excelProcessorInstance.getData()