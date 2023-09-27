'''
#*                            Listas Avanzadas y Diccionarios:
#
#           En Python, las listas y los diccionarios son estructuras de datos fundamentales que permiten almacenar
#           y organizar información. Aquí te explico cómo trabajar con listas avanzadas y diccionarios:
#
#*              Listas Avanzadas:
#
#           Las listas son secuencias ordenadas de elementos que pueden contener cualquier tipo de dato. 
#           Python ofrece características avanzadas para trabajar con listas, como listas por comprensión.
#
#*              Listas por Comprensión:
#           Las listas por comprensión son una forma concisa de crear listas a partir de una expresión y un bucle for.
#           Son útiles para transformar o filtrar datos en una lista.
#
'''
# * Ejemplo

numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]

'''
#          En este ejemplo, estamos creando una nueva lista llamada cuadrados que contiene los cuadrados de los números en la lista numeros.

#*              Métodos de Listas:
    Python proporciona una variedad de métodos para trabajar con listas, 
    como #* append(), extend(), insert(), remove(), pop(), y otros. 
    Estos métodos permiten agregar, eliminar y modificar elementos en una lista.

#*              Diccionarios:

    Los diccionarios son estructuras de datos que almacenan pares clave-valor. 
    Cada elemento en un diccionario tiene una clave única que se utiliza 
    para acceder a su valor correspondiente.

#*              Creación de Diccionarios:
    Puedes crear un diccionario utilizando llaves {}
    y pares clave-valor separados por dos puntos :.
    
'''
# * Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

'''
#*                  Acceso y Modificación de Valores:
    Puedes acceder a los valores de un diccionario utilizando las claves correspondientes 
    y modificarlos si es necesario.
'''
# * Ejemplo

nombre = persona["nombre"]  # Acceder al valor de la clave "nombre"
persona["edad"] = 26  # Modificar el valor de la clave "edad"

'''

#*                  Métodos de Diccionarios:
    Python proporciona métodos para trabajar con diccionarios, 
#*    como keys(), values(), items(), get(), update(), y otros. 
#   Estos métodos permiten realizar diversas operaciones en diccionarios, 
#   como obtener todas las claves, valores o pares clave-valor, 
#   agregar nuevos elementos o actualizar valores existentes.

    Es importante comprender cómo trabajar con listas avanzadas y diccionarios, 
    ya que estas estructuras de datos son ampliamente utilizadas en la programación Python. 
    A medida que tu estudiante avance, podrá aplicar estas técnicas en proyectos más complejos 
    y aplicaciones del mundo real.

'''

'''

#*                  Ejemplo 1: Obtener las Claves y Valores de un Diccionario

        El método keys() devuelve una lista de todas las claves en un diccionario, 
        y el método values() devuelve una lista de todos los valores.
'''

# *Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

claves = persona.keys()
valores = persona.values()

print("Claves:", claves)
print("Valores:", valores)

'''

#*                  Ejemplo 2: Obtener Pares Clave-Valor

        El método items() devuelve una lista de tuplas que contienen pares clave-valor.
'''

# *Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

pares = persona.items()

print("Pares Clave-Valor:", pares)

'''

#*                  Ejemplo 3: Acceder a un Valor por Clave con get()

        El método get() permite acceder a un valor en un diccionario por su clave. 
        Si la clave no existe, en lugar de generar un error, devolverá un valor predeterminado 
        (o None si no se especifica).
        
'''
# *Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

nombre = persona.get("nombre")
telefono = persona.get("telefono", "No disponible")

print("Nombre:", nombre)
print("Teléfono:", telefono)

'''
#*                  Ejemplo 4: Actualizar un Diccionario con update()

        El método update() se utiliza para agregar elementos de otro diccionario 
        o pares clave-valor a un diccionario existente.
        
'''
# *Ejemplo

persona = {"nombre": "Ana", "edad": 25}

nuevos_datos = {"ciudad": "Madrid", "profesion": "Ingeniera"}

persona.update(nuevos_datos)

print("Persona actualizada:", persona)

'''
#*                  Ejemplo 5: Eliminar una Clave-Valor con pop()

        El método pop() se utiliza para eliminar un elemento por su clave y devolver su valor. 
        Si la clave no existe, puedes especificar un valor predeterminado que se devolverá en su lugar.
        
'''
# *Ejemplo

persona = {"nombre": "Ana", "edad": 25,
           "ciudad": "Madrid"}

ciudad = persona.pop("ciudad")  # Elimina la clave "ciudad" y devuelve su valor
# Intenta eliminar la clave "profesion", devuelve "Desconocido" si no existe
profesion = persona.pop("profesion", "Desconocido")

print("Ciudad eliminada:", ciudad)
print("Profesión (predeterminado si no existe):", profesion)
print("Diccionario actualizado:", persona)

'''
#!                  Ejemplo 6: Borrar todos los Elementos con clear()

        El método clear() se utiliza para eliminar todos los elementos de un diccionario, dejándolo vacío.
        
'''

# * Ejemplo
#! PRECAUCION AL UTILIZAR

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

persona.clear()  # Borra todos los elementos del diccionario

print("Diccionario vacío:", persona)

'''

#*                  Ejemplo 7: Copiar un Diccionario con copy()

        El método copy() se utiliza para crear una copia superficial de un diccionario. 
        Esto significa que los valores se copian, pero no los objetos a los que hacen referencia.
        
'''

# *Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

copia_persona = persona.copy()  # Crea una copia superficial del diccionario

print("Copia del diccionario:", copia_persona)

'''
#*                  Ejemplo 8: Combinar Dos Diccionarios con update()

        Puedes combinar dos diccionarios usando el método update().

'''

# *Ejemplo

diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4}

# Combina diccionario1 con diccionario2, sobrescribiendo las claves duplicadas con los valores de diccionario2
diccionario1.update(diccionario2)

print("Diccionario combinado:", diccionario1)

'''
#*                  Ejemplo 9: Recorrer un Diccionario con un Bucle for

        Puedes utilizar un bucle for para recorrer las claves y los valores de un diccionario.

'''

# *Ejemplo

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
