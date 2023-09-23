'''
#*                  Manipulación de Archivos:

    Enseña cómo abrir, leer, escribir y elimnar archivos en Python.
    Muestra cómo cerrar archivos adecuadamente después de su uso.

#*                  Explicacion de codigo

   1) Abre un archivo llamado "archivo.txt" en modo escritura ("w"). 
    Si el archivo no existe, se creará. Si ya existe, su contenido se sobrescribirá.

   2) Crea un contexto de manejo de archivos utilizando la declaración with. 
        Esto garantiza que el archivo se cierre correctamente después de que 
            se realicen todas las operaciones en él, incluso si ocurren excepciones.

   3) Dentro del contexto, se utiliza el objeto de archivo archivo para escribir la cadena 
        "Hola, mundo" en el archivo.

   4) Una vez que se completa la escritura, el archivo se cierra automáticamente debido al uso de
        la declaración with, lo que garantiza que los cambios se guarden correctamente 
            y se liberen los recursos del archivo.
'''

import os
"""  # Todo Quitar Comillas para realizar ejemplo
# ? With se usa para cerrar arcicho automaticamente despues de escribir
# ? Abre y/o crea archivo para escritura
with open("archivo.txt", "w") as archivo:
    # ? ingresa informacion
    archivo.write("Hola, mundo")

"""  # Todo Quitar Comillas para realizar ejemplo

# """
'==========================================================='
# """

'''
#*                  Ejemplo de escritura con multiples lineas ==> \n


    En este ejemplo, el archivo se abre en modo escritura ("w"), 
    lo que significa que podemos escribir datos en él. 
    El with se usa para garantizar que el archivo se cierre automáticamente después de su uso.

    Escribir en un archivo: Una vez que el archivo está abierto en modo escritura,
    puedes usar el método .write() para escribir datos en el archivo:
'''

"""  # Todo Quitar Comillas para realizar ejemplo

with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")
    archivo.write("Este es un archivo de ejemplo\n")

"""  # Todo Quitar Comillas para realizar ejemplo

# """
'==========================================================='
# """

'''
#*                  En este ejemplo, escribimos dos líneas de texto en el archivo.

#*      Leer desde un archivo: Para leer datos desde un archivo, 
    #        1) Debemos abrirlo en modo lectura ("r"). 
    #        2) Luego, podemos usar métodos como .read(), .readline(), o .readlines() 
    #             para leer contenido del archivo.
'''
"""  # Todo Quitar Comillas para realizar ejemplo

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

"""  # Todo Quitar Comillas para realizar ejemplo

# Explicacion
'''
  #?  .read(): Lee todo el contenido del archivo en una sola cadena.
  #?  .readline(): Lee una línea del archivo a la vez.
  #?  .readlines(): Lee todas las líneas del archivo en una lista de cadenas.

#*      Cerrar un archivo: Después de trabajar con un archivo, es importante cerrarlo para liberar recursos y asegurarse de que los cambios se guarden. 
#*       El uso de with como se mostró en los ejemplos anteriores asegura que el archivo se cierre automáticamente cuando se sale del bloque with.
'''

# """
'==========================================================='
# """

'''
#*                  Manejo de errores: 
#       
#           Cuando trabajamos con archivos, es importante manejar posibles errores, 
#                   como la falta de un archivo o problemas de permisos. 
#           Esto se hace utilizando bloques try y except para capturar excepciones:
'''
"""  # Todo Quitar Comillas para realizar ejemplo

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
except IOError:
    print("Error al leer el archivo.")


"""  # Todo Quitar Comillas para realizar ejemplo

# """
'==========================================================='
# """

#!  Elimnar Archivo Anterior (Permanente)

# * Codigo a Utilizar (quitar comillas)

#! PRECAUCION !#


"""  # Todo Quitar Comillas para realizar ejemplo

archivo_a_eliminar = "archivo.txt"  # Reemplaza esto con el nombre de tu archivo

# Verificamos si el archivo existe antes de intentar eliminarlo
if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)
    print(f"El archivo '{archivo_a_eliminar}' ha sido eliminado.")
else:
    print(f"El archivo '{archivo_a_eliminar}' no existe.")

"""  # Todo Quitar Comillas para realizar ejemplo
