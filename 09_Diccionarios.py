'''
#*          ¿Qué son los Diccionarios?

A diferencia de las listas que vimos anteriormente, 
los diccionarios son estructuras de datos en Python que almacenan pares clave-valor. 
Cada elemento en un diccionario tiene una clave única que se utiliza 
para acceder a su valor correspondiente. Los diccionarios son extremadamente útiles 
cuando necesitas asociar datos o atributos con un identificador único.

Para crear un diccionario en Python, 
usa llaves {} y separa cada par clave-valor con dos puntos ':'
Por ejemplo:
'''
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Miami"}
'''
#*           Operaciones con Diccionarios:

Los diccionarios admiten una variedad de operaciones y métodos que 
te permiten trabajar con sus elementos. 

Algunas operaciones comunes en diccionarios incluyen:

  *  Agregar elementos: Puedes agregar un nuevo par clave-valor asignando un valor a una nueva clave.
  
  *  Eliminar elementos: Puedes eliminar un par clave-valor utilizando la palabra clave del.
  
  *  Acceder a valores: Puedes acceder a un valor utilizando la clave correspondiente.
  
'''
'''
#*          Crear y Manipular un Diccionario:

Supongamos que estamos construyendo un diccionario para almacenar información sobre un estudiante, 
como su nombre, edad y calificaciones. 

Aquí está cómo crear y manipular este diccionario:
'''
# Crear un diccionario para un estudiante
estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "calificaciones": [85, 90, 78, 92, 88]
}

# Acceder a valores en el diccionario
nombre_estudiante = estudiante["nombre"]
edad_estudiante = estudiante["edad"]
calificaciones_estudiante = estudiante["calificaciones"]

# Agregar una nueva calificación
estudiante["calificaciones"].append(95)

# Imprimir la información del estudiante
print(f"Nombre: {nombre_estudiante}")
print(f"Edad: {edad_estudiante}")
print(f"Calificaciones: {calificaciones_estudiante}")

'''
En este ejemplo, 
creamos un diccionario llamado estudiante que contiene información sobre un estudiante ficticio. 
Luego, accedemos a los valores en el diccionario utilizando las claves correspondientes y 
agregamos una nueva calificación a la lista de calificaciones.
'''

# *          Ejemplo 2: Recorrer un Diccionario con un Bucle for:
'Supongamos que queremos recorrer el diccionario de estudiantes para imprimir la información de cada estudiante:'

# Diccionario de estudiantes
estudiantes = {
    "estudiante1": {"nombre": "Juan", "edad": 20},
    "estudiante2": {"nombre": "María", "edad": 22},
    "estudiante3": {"nombre": "Carlos", "edad": 21}
}

# Recorrer el diccionario e imprimir la información de cada estudiante
for clave, info_estudiante in estudiantes.items():
    nombre = info_estudiante["nombre"]
    edad = info_estudiante["edad"]
    print(f"{clave}: Nombre: {nombre}, Edad: {edad}")

'''
En este ejemplo, tenemos un diccionario llamado estudiantes que contiene información sobre varios estudiantes. 
Utilizamos un bucle for para recorrer el diccionario y mostrar la información de cada estudiante.

Estos son solo dos ejemplos simples de cómo trabajar con diccionarios en Python. 
Los diccionarios son muy útiles para organizar y acceder a datos de manera eficiente, 
especialmente cuando necesitas relacionar información utilizando claves únicas.
'''
