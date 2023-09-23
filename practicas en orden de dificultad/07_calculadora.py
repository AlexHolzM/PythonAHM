
# *                  Calculadora
#   Crea una calculadora simple que pueda realizar operaciones de:
#   suma, resta, multiplicación y división.
#   Pídele al usuario que ingrese dos números y una operación,
# y luego muestra el resultado.

print('Elige el tipo de operacion aritmetica deseada.')
print('+', '-', '*', '/')
operador = input('ingrese eleccion: ')
n1 = float(input('ingresa el primer numero: '))
n2 = float(input('ingresa el segundo numero: '))

for t in operador:
    if t == '+':
        suma = n1+n2
        print(suma)
    elif t == '-':
        resta = n1-n2
        print(resta)
    elif t == '*':
        multi = n1*n2
        print(multi)
    elif t == '/':
        div = n1/n2
        print(div)
    else:
        print('el operador no esta disponible')
