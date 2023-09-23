import statistics  # Importa libreria de estadística para cálculo

A1 = 'Roberto'
c1 = [10, 6, 7, 5, 7, 10, 10, 8, 10, 10]

print('Lista de calificaciones de', A1, ':', c1)

# * Usando Ciclo For

suma_calificaciones = 0
for calificacion in c1:
    suma_calificaciones += calificacion

promedio = suma_calificaciones / len(c1)
print('El promedio de calificaciones es de:', promedio)

mensaje = ''

if promedio == 10:
    mensaje = A1 + ' Aprobaste con Honores!!'
elif 8.5 <= promedio <= 9.4:
    mensaje = A1 + ' Aprobaste Satisfactoriamente!'
elif 9.5 <= promedio < 10:
    mensaje = A1 + ' Aprobaste Sobresalientemente!'
elif 7 <= promedio <= 8.4:
    mensaje = A1 + ' Aprobaste, sigue esforzándote más!'
else:
    mensaje = A1 + ' Lamento que no hayas aprobado el curso, tienes que estudiar más'

print(mensaje)
