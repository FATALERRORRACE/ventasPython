import os
from services.excelProcessor_service import ExcelProcessor
class dataReader:
    def __init__(self):
        filePath = input("Ingrese la ruta de directorio del archivo, si deja el campo vacío el sistema buscará en la raíz del proyecto un archivo excel: ")
        if not filePath:
            for f in os.listdir(os.getcwd()):
                if f.lower().endswith('.xlsx'):
                    filePath = os.path.join(os.getcwd(), f)
                    print(f"Archivo encontrado: {filePath}")
                    break
            else:
                print("No se encontró ningún archivo .xlsx en la raíz del proyecto.")
                return
        if os.path.exists(filePath) == False:
            #GENERAR LOOP DE RESPUESTAS
            print(f"El archivo '{filePath}' no existe.")
            return
        sheetName = input("Ingrese el nombre de la hoja a procesar, si dejas el campo vacío se usará \"Sheet1\" por defecto: ")
        #GENERAR LOOP DE RESPUESTAS AQUÍ TAMBIÉN

        excelProcessorInstance = ExcelProcessor(filePath, (sheetName if sheetName else "Sheet1"))
        excelProcessorInstance.getData()