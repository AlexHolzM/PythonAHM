'''
#*              Listas:

    Una lista en Python es una colección ordenada de elementos.
    Los elementos en una lista pueden ser de cualquier tipo de datos, 
    como números, cadenas de texto, otros objetos, o incluso otras listas.
    Las listas se crean utilizando corchetes [] y los elementos se separan por comas.
    Los elementos en una lista tienen un índice basado en cero, 
    lo que significa que el primer elemento tiene un índice de 0, 
    el segundo tiene un índice de 1, y así sucesivamente.
   
    Ejemplo de creación de una lista:                       '''

mi_lista = [1, 2, 3, "Hola", "Mundo"]
print(mi_lista)

'''
    Puedes acceder a elementos específicos de una lista utilizando 
    la notación de corchetes y su índice. 
    Por ejemplo, mi_lista[0] accederá al primer elemento (1 en este caso).
'''
mi_lista = [1, 2, 3, "Hola", "Mundo"]
print(mi_lista[0])


'''
#*              Diccionarios:

    Un diccionario en Python es una colección no ordenada de pares clave-valor.
    Cada elemento en un diccionario consiste en una clave y su valor asociado. Las claves son únicas dentro de un diccionario.
    Los diccionarios se crean utilizando llaves {} y los pares clave-valor se separan por comas. Cada par clave-valor se separa por :.
    Ejemplo de creación de un diccionario:  '''

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

'''
    Puedes acceder a los valores de un diccionario utilizando la clave correspondiente. 
    Por ejemplo, mi_diccionario["nombre"] devolverá "Juan".
'''
# Por ejemplo
print(mi_diccionario["nombre"])
# devolverá "Juan".'''

'''
#*              Operaciones comunes:

    Para ambas estructuras de datos, puedes realizar operaciones comunes como 
    agregar elementos, eliminar elementos, modificar elementos, contar elementos y más.
    Por ejemplo, para agregar un elemento a una lista, puedes usar append(), 
    y para agregar un par clave-valor a un diccionario, puedes asignarlo directamente a una nueva clave.
    
    Ejemplo de agregar un elemento a una lista: #*                mi_lista.append(4)
    
    Ejemplo de agregar un par clave-valor a un diccionario:#*     mi_diccionario["profesion"] = "Programador"
'''
mi_lista.append(4)
mi_diccionario["profesion"] = "Programador"
print(mi_lista)
print(mi_diccionario)
