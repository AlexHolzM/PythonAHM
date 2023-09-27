'''
#*          ¿Qué son las Listas?

Las listas son una de las estructuras de datos más comunes en Python 
y se utilizan para almacenar colecciones de elementos. 
Puedes pensar en una lista como una secuencia ordenada de elementos que 
pueden ser de diferentes tipos, como números, cadenas de texto, u otros objetos. 
Las listas son muy versátiles y se utilizan para almacenar y manipular datos de manera eficiente.

Para crear una lista en Python, 
simplemente coloca los elementos entre corchetes [] y sepáralos por comas. 
Por ejemplo:
'''
mi_lista = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
'''
#*          Operaciones con Listas:

Las listas admiten una variedad de operaciones y métodos 
que te permiten trabajar con sus elementos. 
Algunas operaciones comunes en listas incluyen:

   *    Agregar elementos: Puedes agregar elementos al final de una lista utilizando append() 
        o en una posición específica usando insert().
        
   *    Eliminar elementos: Puedes eliminar elementos por valor con remove() o por índice con pop().
   
   *    Acceder a elementos: Puedes acceder a elementos individuales utilizando índices 
        (los índices comienzan en 0).
   
   *     Longitud de una lista: Puedes obtener la longitud de una lista con la función len().
'''
# * Ejemplo 1: Crear una lista con nombres de frutas y mostrar la primera y última fruta de la lista:
frutas = ["manzana", "banana", "cereza"]
primera_fruta = frutas[0]
ultima_fruta = frutas[-1]

print("Primera fruta:", primera_fruta)
print("Última fruta:", ultima_fruta)
'''
En este ejemplo, creamos una lista llamada frutas que contiene tres nombres de frutas. 
Luego, accedemos al primer elemento usando el índice 0 (frutas[0]) 
y al último elemento usando el índice -1 (frutas[-1]). Finalmente, imprimimos ambos valores.
'''
# * Ejemplo 2: Agregar una nueva fruta a la lista y eliminar una fruta existente:
frutas = ["manzana", "banana", "cereza"]

# Agregar una nueva fruta al final de la lista
frutas.append("uva")

# Eliminar la fruta "banana"
frutas.remove("banana")

print("Frutas después de agregar y eliminar:", frutas)
'''
En este ejemplo, utilizamos el método append() para agregar la fruta "uva" al final de la lista 
y luego usamos el método remove() para eliminar la fruta "banana". 
La lista resultante se imprime para mostrar los cambios.
'''
# * Ejemplo 3: Usar un bucle for para recorrer y mostrar todos los elementos de la lista de frutas:
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
'''
En este ejemplo, utilizamos un bucle for para iterar a través de la lista de frutas y mostrar cada fruta en una línea. 
El bucle for toma cada elemento de la lista uno por uno y lo almacena en la variable fruta, que luego se imprime.
'''
