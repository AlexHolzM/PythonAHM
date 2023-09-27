'''
#*          Definición de Funciones en Python:

En Python, las funciones se definen utilizando la palabra clave def, 
seguida del nombre de la función y paréntesis que pueden contener los 
parámetros de entrada. Por ejemplo:
'''


def saludar(nombre):
    print("Hola, " + nombre + "!")


'''
En este ejemplo, hemos definido una función llamada saludar
que toma un parámetro nombre y muestra un saludo personalizado.

#*           Llamada de Funciones:

Una vez que has definido una función, puedes llamarla en 
cualquier parte de tu programa para ejecutar el código dentro de ella. 
Para llamar una función, simplemente escribe su nombre seguido de paréntesis y, 
si es necesario, proporciona los argumentos requeridos.
'''
saludar("Juan")
# Este código llama a la función saludar con el argumento "Juan" y mostrará "Hola, Juan!" como resultado.

'''
Ejercicio práctico:

Definamos una función que calcule el área de un triángulo utilizando la fórmula: 
Área = (base * altura) / 2. Luego, llamemos a esta función con valores específicos.
'''


def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# Llamamos a la función
resultado = calcular_area_triangulo(5, 8)
print("El área del triángulo es:", resultado)
'''
En este ejercicio, hemos definido una función calcular_area_triangulo 
que acepta dos parámetros (base y altura) y devuelve el área calculada. 
Después, llamamos a la función y mostramos el resultado.
'''
