
# *          Uso Avanzado de Excepciones:

# ?          Bloque finally:

'''
En Python, además de los bloques try y except, 
tenemos el bloque finally. 
Este bloque se utiliza para definir código que se ejecutará siempre, 
independientemente de si se produce una excepción o no. 
Es útil para realizar tareas de limpieza, como 
cerrar archivos o conexiones a bases de datos, después de manejar una excepción.

Aquí tienes un ejemplo:
'''
try:
    # Intentar realizar una operación que podría generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Este bloque se ejecuta siempre, haya excepción o no.")
    # En este ejemplo, se intenta una división por cero que generará una excepción.
    # Aunque se captura la excepción en el bloque except,
    # el bloque finally se ejecutará después de manejar la excepción.

 # ===============================================================================================

# ?          Lanzar Excepciones Personalizadas:

'''
En algunas situaciones, es útil definir tus propias excepciones personalizadas 
para manejar casos específicos en tu programa. Puedes crear tus propias clases de excepción 
derivadas de la clase base Exception y lanzarlas cuando sea necesario.
'''


class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


try:
    # Lanzar una excepción personalizada
    raise MiExcepcionPersonalizada("Esto es una excepción personalizada")
except MiExcepcionPersonalizada as e:
    print("Se capturó una excepción personalizada:", e.mensaje)
    # En este ejemplo, definimos una clase MiExcepcionPersonalizada que hereda de Exception
    # y tiene un constructor que toma un mensaje. Luego, lanzamos esta excepción personalizada
    # y la capturamos en el bloque except.

 # ===============================================================================================

# ?           Mejores Prácticas de Manejo de Excepciones:

'''
    Repasaremos algunas mejores prácticas de manejo de excepciones, 
    como evitar capturar excepciones demasiado generales 
    y proporcionar información útil en los mensajes de error.
'''
# * Captura excepciones específicas:
# En lugar de capturar excepciones demasiado generales, como Exception,
# intenta capturar solo las excepciones que esperas manejar.
# Esto hace que tu código sea más robusto y ayuda a
# identificar problemas específicos más fácilmente.
# ? Por ejemplo:

'''
try:
    #? Código que puede generar una excepción específica
except MiExcepcionEspecifica:
    #? Manejar la excepción específica
'''
# * Proporciona mensajes de error informativos:
# Cuando captures una excepción, considera proporcionar un mensaje de error descriptivo
# para que sea más fácil depurar problemas.
# Esto es útil tanto para ti como para otros desarrolladores que puedan trabajar en tu código.
# ? Por ejemplo:
'''
    try:
    #? Código que puede generar una excepción
except MiExcepcionEspecifica as e:
    print(f"Error: {e}")
'''
# *Usa el bloque finally:
# El bloque finally se utiliza para realizar tareas de limpieza,
# como cerrar archivos o conexiones a bases de datos,
# después de manejar una excepción.
# Esto garantiza que las tareas de limpieza se realicen
# incluso si se produce una excepción.
# ? Por ejemplo:
'''
    try:
    # Código que puede generar una excepción
except MiExcepcionEspecifica as e:
    # Manejar la excepción específica
finally:
    # Realizar tareas de limpieza
'''

#! Evita el uso excesivo de excepciones:
# Las excepciones no deben usarse para el flujo de control normal de un programa.
# Evita usar excepciones como parte de la lógica regular de tu programa,
# ya que esto puede hacer que el código sea menos legible y eficiente.

# * Documenta las excepciones:
# Asegúrate de documentar las excepciones que pueden generarse en tus funciones
# o métodos para que otros desarrolladores sepan qué excepciones esperar y cómo manejarlas.

# ? Usa el contexto de gestión de archivos: Para trabajar con archivos,
# considera utilizar el bloque with que proporciona un contexto de gestión de archivos.
# Esto garantiza que el archivo se cierre automáticamente al salir del bloque,
# incluso si se produce una excepción.

# #? Por ejemplo:
'''    
    with open("archivo.txt", "r") as archivo:    (ver manipular_archivos.py)
    # Trabajar con el archivo dentro de este bloque
    # El archivo se cierra automáticamente fuera del bloque

'''
