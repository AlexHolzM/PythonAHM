'''
Usando condicional if
'''
import statistics  # Importa libreria de estadisctica para calculo

A1 = 'Roberto'
c1 = [10, 10, 0, 0, 10, 0, 0, 0, 0, 0]
print('lista de calificaciones de', A1, ':', c1)
promedio = statistics.mean(c1)
print('el promedio de calificaiones es de:', promedio)

if promedio == 10:
    print(A1, 'Aprovaste con Honores!!')
elif promedio >= 8.5 and promedio <= 9.4:
    print(A1, 'Aprovaste Satisfactoriamente!')
elif promedio >= 9.5 and promedio < 10:
    print(A1, 'Aprovaste Sobresalientemente!')
elif promedio >= 7 and promedio <= 8.4:
    print(A1, 'Aprovaste sigue esforzandote mas!')
else:
    print(A1, 'Lamento que no hayas aprovado el curso tienes que estudiar mas')
