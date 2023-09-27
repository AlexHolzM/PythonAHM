'''
#*          Una de las ventajas clave de utilizar funciones es la modularidad. 

La modularidad se refiere a la capacidad de dividir un programa en partes más pequeñas y manejables, 
donde cada parte (o función) tiene una tarea específica. Esto hace que el código sea más organizado 
y más fácil de mantener.

La reutilización del código es otro beneficio importante de las funciones. 
Una vez que has definido una función para realizar una tarea específica, 
puedes llamarla en múltiples lugares de tu programa sin tener que volver a escribir el mismo código 
una y otra vez. Esto ahorra tiempo y reduce la posibilidad de errores.
'''
'''
#*          Funciones Incorporadas en Python:

Python proporciona una serie de funciones incorporadas que puedes utilizar en tus programas 
sin necesidad de definirlas. Algunos ejemplos comunes de funciones incorporadas en Python son:

    *   print(): Se utiliza para imprimir texto o valores en la consola.
    *   len(): Devuelve la longitud (número de elementos) de una secuencia, como una lista o una cadena.
    *   input(): Permite al usuario ingresar datos desde el teclado.
    *   range(): Genera una secuencia de números.
'''
mensaje = "Hola, Python"
print(mensaje)  # Imprime el mensaje en la consola
longitud = len(mensaje)  # Calcula la longitud de la cadena
nombre = input("Ingresa tu nombre: ")  # Solicita entrada del usuario
numeros = list(range(1, 6))  # Genera una lista de números del 1 al 5
print(numeros)
'''
Ejercicio 1: Crea una función llamada es_par que tome un número como argumento 
y devuelva True si es par y False si es impar.
'''


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero1 = 4
numero2 = 7
resultado1 = es_par(numero1)
resultado2 = es_par(numero2)

print(f"¿{numero1} es par? {resultado1}")  # Debería imprimir "¿4 es par? True"
# Debería imprimir "¿7 es par? False"
print(f"¿{numero2} es par? {resultado2}")

'''
Ejercicio 2: Define una función llamada calcular_promedio que acepte una lista de números 
y calcule su promedio.
'''


def calcular_promedio(numeros):
    if len(numeros) == 0:
        return None  # Manejar el caso de una lista vacía
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio


# Probemos la función
lista_numeros1 = [10, 20, 30, 40, 50]
lista_numeros2 = [5, 15, 25]

promedio1 = calcular_promedio(lista_numeros1)
promedio2 = calcular_promedio(lista_numeros2)
promedio3 = calcular_promedio([])  # Prueba con una lista vacía

# Debería imprimir "El promedio de [10, 20, 30, 40, 50] es: 30.0"
print(f"El promedio de {lista_numeros1} es: {promedio1}")
# Debería imprimir "El promedio de [5, 15, 25] es: 15.0"
print(f"El promedio de {lista_numeros2} es: {promedio2}")
# Debería imprimir "El promedio de una lista vacía es: None"
print(f"El promedio de una lista vacía es: {promedio3}")


'''
Ejercicio 3: Escribe una función llamada inverso que tome una cadena y devuelva la cadena al revés. 
Por ejemplo, si se le pasa "Python", debe devolver "nohtyP".
'''


def inverso(cadena):
    cadena_al_reves = cadena[::-1]
    return cadena_al_reves


# Probemos la función
cadena1 = "Python"
cadena2 = "Hola, mundo!"

resultado1 = inverso(cadena1)
resultado2 = inverso(cadena2)

# Debería imprimir "El inverso de 'Python' es: 'nohtyP'"
print(f"El inverso de '{cadena1}' es: '{resultado1}'")
# Debería imprimir "El inverso de 'Hola, mundo!' es: '!odnum ,aloH'"
print(f"El inverso de '{cadena2}' es: '{resultado2}'")
