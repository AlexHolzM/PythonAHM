'''

#*                  Trabajo con Datos Estructurados:
#
#           En la programación, a menudo nos encontramos con la necesidad de trabajar con 
#           datos estructurados almacenados en archivos, como datos tabulares en formato CSV o 
#           datos estructurados en formato JSON. 
#           A continuación, te explicaré cómo trabajar con estos dos formatos:

#*              CSV (Comma-Separated Values):

#           Los archivos CSV son una forma común de almacenar datos tabulares, 
#           como hojas de cálculo. Los datos se separan por comas o 
#           algún otro carácter delimitador, y cada fila representa un registro.
#
#*              Lectura de un archivo CSV:
#        
#           Para leer un archivo CSV en Python, primero debes importar el módulo csv. 
#           Luego, puedes utilizar el módulo para abrir el archivo CSV, leer sus contenidos y procesarlos.
#

'''
import json
import csv
with open("datos.csv", "r") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)

'''
#*           El código anterior abre el archivo "datos.csv" en modo lectura 
#               y utiliza un lector CSV para leer cada fila del archivo e imprimir sus valores.
#
#*           Escritura en un archivo CSV:
#               Para escribir datos en un archivo CSV, puedes utilizar el módulo csv de la siguiente manera:
#

'''

datos = [
    ["Nombre", "Edad"],
    ["Ana", 25],
    ["Juan", 30],
    ["Karla", 28]
]
with open("nuevos_datos.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)

'''

#*            El código anterior crea un archivo "nuevos_datos.csv" en modo escritura 
#               y utiliza un escritor CSV para escribir los datos proporcionados en forma de lista.
#
#*              JSON (JavaScript Object Notation):
#
#*           JSON es un formato de datos ligero que se utiliza ampliamente para 
#             el intercambio de datos entre aplicaciones. 
#               En Python, puedes trabajar con datos JSON utilizando el módulo json.
#
#*              Lectura de un archivo JSON:
#
#*           Para leer un archivo JSON en Python, primero debes importar el módulo json.
#              Luego, puedes abrir el archivo JSON, leer su contenido y analizarlo.
#

'''

with open("datos.json", "r") as archivo_json:
    datos = json.load(archivo_json)
    print(datos)

'''

#*              El código anterior abre el archivo "datos.json" en modo lectura,
#                   carga su contenido en una estructura de datos Python y luego imprime los datos.
#
#*              Escritura en un archivo JSON:
#                   Para escribir datos en un archivo JSON, puedes utilizar el módulo json de la siguiente manera:

'''

datos = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
with open("nuevos_datos.json", "w") as archivo_json:
    json.dump(datos, archivo_json)

'''

#*              El código anterior crea un archivo "nuevos_datos.json" en modo escritura
#                   y utiliza la función json.dump() para escribir los datos proporcionados en formato JSON.
#
#*              Trabajar con datos estructurados es esencial en el desarrollo de aplicaciones y análisis de datos. 
#                   Asegúrate de que tu estudiante practique la lectura y escritura de archivos CSV y JSON
#                   para adquirir experiencia en el manejo de datos estructurados en Python.
#
#
'''
