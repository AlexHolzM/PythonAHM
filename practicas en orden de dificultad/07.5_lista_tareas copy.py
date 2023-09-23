
# *                  Lista de Tareas

'Permite crear una lista agregando elementos'

lista_tareas = []
# Pedir al usuario que ingrese datos hasta que decida salir
while True:
    # Pedir al usuario que ingrese un elemento
    tareas = input("Ingresa un elemento (o escribe 'salir' para terminar): ")

    # Verificar si el usuario quiere salir
    if tareas.lower() == 'salir':
        break

    # Agregar el elemento a la lista
    lista_tareas.append(tareas)

# Mostrar la lista resultante
print("La lista final es:")
print(lista_tareas)
