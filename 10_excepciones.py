'''
#?                  ¿Qué son las Excepciones?

#   Las excepciones son eventos inesperados o errores que pueden ocurrir durante la ejecución de un programa. 
# Estos eventos pueden detener la ejecución normal del programa si no se manejan adecuadamente. 
# Las excepciones son una parte fundamental de la programación y son utilizadas 
# para lidiar con situaciones excepcionales, como divisiones por cero, 
# acceso a archivos que no existen o conversiones de tipos incorrectas.

#*                  Gestión de Excepciones:

    La gestión de excepciones en Python se realiza mediante bloques try y except. 
    Estos bloques permiten que el programa capture y maneje errores de manera adecuada 
    en lugar de detenerse abruptamente. A continuación, se describe el proceso:

    Bloque try: En este bloque, colocamos el código que puede generar una excepción. 
    Python intentará ejecutar este código.

    Bloque except: Si se produce una excepción dentro del bloque try, 
    el control se transfiere al bloque except. Aquí es donde especificamos 
    cómo deseamos manejar el error.
    
'''

# *       Manejo de excepciones

"""  # Todo Quitar Comillas para realizar ejemplo

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError:
    # Manejo de la excepción ZeroDivisionError
    print("¡Error! División por cero.")


"""  # Todo Quitar Comillas para realizar ejemplo

'''
#*          En este ejemplo, estamos intentando dividir 10 por 0, 
#*          lo que generará un ZeroDivisionError. Hemos especificado que, 
#*          si eso sucede, imprimiremos un mensaje de error personalizado.

'''

# """
'==========================================================='
# """

# *  Tipos de Excepciones Comunes:

'''Existen muchos tipos diferentes de excepciones en Python, 
cada una diseñada para manejar situaciones específicas de error. 
Algunos ejemplos comunes de excepciones incluyen:


#    ZeroDivisionError: Se produce cuando intentas dividir por cero.
#    TypeError: Se produce cuando realizas una operación no válida para un tipo de dato específico.
#    FileNotFoundError: Se produce cuando intentas acceder a un archivo que no existe.
'''

# * Ejemplo Practico

try:
    # Solicitar al usuario ingresar dos números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Realizar la división
    resultado = numero1 / numero2

    # Mostrar el resultado
    print(f"El resultado de la división es: {resultado}")

except ValueError:
    print("Error: Debes ingresar números válidos.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# """
'======================Explicaciones Detalladas========================'
# """

'''
#*                  Múltiples Bloques except: 
# 
#           Puedes tener varios bloques except para manejar diferentes tipos de excepciones. 
#           Esto te permite manejar errores específicos de manera adecuada.

'''
"""  # Todo Quitar Comillas para realizar ejemplo

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError:
    # Manejo de la excepción ZeroDivisionError
    print("¡Error! División por cero.")
except FileNotFoundError:
    # Manejo de la excepción FileNotFoundError
    print("¡Error! Archivo no encontrado.")

"""  # Todo Quitar Comillas para realizar ejemplo

'''
#*          Bloque else: 
#       Opcionalmente, puedes usar un bloque else después de los bloques except.
#       El código en el bloque else se ejecuta si no se produce ninguna excepción en el bloque try.
'''

"""  # Todo Quitar Comillas para realizar ejemplo

try:
    resultado = 10 / 5  # Esto no generará una excepción
except ZeroDivisionError:
    print("¡Error! División por cero.")
else:
    print("La división fue exitosa. El resultado es:", resultado)

"""  # Todo Quitar Comillas para realizar ejemplo

# """
'==========================================================='
# """

'''
#*                  Bloque finally: 
#           También puedes usar un bloque finally opcional que se ejecutará siempre, 
#           independientemente de si se generó una excepción o no. 
#           Esto se utiliza comúnmente para realizar tareas de limpieza, 
#           como cerrar archivos o conexiones de bases de datos.
#
'''

"""  # Todo Quitar Comillas para realizar ejemplo

try:
    archivo = open("mi_archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("¡Error! Archivo no encontrado.")
finally:
    archivo.close()  # Cerramos el archivo sin importar si hubo una excepción o no
    
"""  # Todo Quitar Comillas para realizar ejemplo

'''
            La gestión de excepciones es una técnica importante para escribir programas robustos y resistentes a errores. 
            Ayuda a garantizar que, incluso si ocurren problemas durante la ejecución, 
            el programa no se bloqueará y se puede proporcionar información significativa sobre el error. 
            A medida que tu estudiante avance en la programación, aprenderá a identificar y 
            manejar adecuadamente las excepciones que puedan surgir en sus programas.
'''

# """
'==========================================================='
# """
