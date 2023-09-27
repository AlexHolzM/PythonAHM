
# *      Abrir y Cerrar Archivos:

# En Python, puedes trabajar con archivos de texto utilizando la función #* open().
# Esta función toma dos argumentos:
# el nombre del archivo que deseas abrir y el modo en el que deseas abrirlo
# (lectura, escritura, anexar, etc.).

# ? Aquí tienes un ejemplo de cómo abrir un archivo para lectura:

archivo = open("mi_archivo.txt", "r")

# Y para cerrar el archivo después de trabajar con él, puedes usar el método #* close():

archivo.close()

#! Es importante cerrar los archivos después de usarlos para liberar los recursos del sistema.
'=============================================================================================='

# *       Leer y Escribir Archivos de Texto:


#        Una vez que has abierto un archivo para lectura,
#        puedes leer su contenido utilizando varios métodos,
#        como,
# *       read()
#              que lee todo el contenido del archivo, o
# *       readline()
#                   , que lee una línea a la vez.

'Aquí tienes un ejemplo de lectura de un archivo:'
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# *      Para escribir en un archivo:
#
#   debes abrirlo en modo de escritura ("w").
#   Puedes utilizar el método write()
#   para agregar datos al archivo.

archivo = open("mi_archivo.txt", "w")
archivo.write("Este es un ejemplo de escritura en un archivo.")
archivo.close()

#!  Recuerda que, al abrir un archivo en modo escritura, su contenido anterior se sobrescribirá.
'=============================================================================================='

# *                      Ejemplos Prácticos con Archivos de Texto:

# ?         Ejemplo 1: Leer un archivo de texto e imprimir su contenido:

'   Supongamos que tienes un archivo de texto llamado "mi_archivo.txt" con el siguiente contenido:'

'''             Este es un ejemplo de archivo de texto.
                Python es un lenguaje de programación poderoso.
                Aprender Python es divertido.
'''

'   Puedes utilizar el siguiente código para leer el contenido de este archivo y luego imprimirlo:  '

# Abrir el archivo para lectura
archivo = open("mi_archivo.txt", "r")

# Leer y almacenar el contenido del archivo
contenido = archivo.read()

# Cerrar el archivo
archivo.close()

# Imprimir el contenido
print(contenido)

# ?          Ejemplo 2: Crear un nuevo archivo de texto y escribir en él:

'       Puedes crear un nuevo archivo de texto y escribir en él utilizando el siguiente código:         '

# Abrir un nuevo archivo para escritura (se creará si no existe)
archivo = open("nuevo_archivo.txt", "w")

# Escribir datos en el archivo
archivo.write("Este es un nuevo archivo de texto.\n")
archivo.write("Puedes agregar varias líneas de texto.\n")
archivo.write("¡Espero que este ejemplo sea útil!")

# Cerrar el archivo
archivo.close()

# *      Este código abrirá un nuevo archivo llamado "nuevo_archivo.txt" en modo de escritura ("w"),
# *      y luego escribirá tres líneas de texto en él.
# *      El \n al final de cada línea representa un salto de línea.

# *      Después de ejecutar este código,
# *      encontrarás un nuevo archivo de texto llamado "nuevo_archivo.txt"
# *     en tu directorio de trabajo con el contenido especificado.
