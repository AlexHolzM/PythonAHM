
# *Estructura condicional 'if'

edad = 13
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("")
# * Bucles (Loops) 'for, while'

# * Bucle for para imprimir números del 1 al 5
# For
print('Bucle For')
for i in range(1, 6):
    print(i)

# While
print('Bucle While')
contador = 0
while True:
    print("Iteración:", contador)
    contador += 1
    if contador >= 5:
        break
print("Bucle while terminado.")


# * Funciones  'def'
# Definición de una función
def saludar(nombre):
    print("Hola,", nombre)


# ? Como Llamar a Funciones?
# Llamando a la función
saludar("Ana")
