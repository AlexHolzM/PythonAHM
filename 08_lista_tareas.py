
# *                  Lista de Tareas con base de datos .JSON

'''
    Crea un programa que permita al usuario gestionar una lista de tareas. 
       - Debe poder agregar tareas, 
       - marcar tareas como completadas 
       - ver la lista de tareas pendientes.

'''
import json

# Función para cargar la lista de tareas desde un archivo JSON


def cargar_lista_tareas():
    try:
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para guardar la lista de tareas en un archivo JSON


def guardar_lista_tareas():
    with open('tareas.json', 'w') as archivo:
        json.dump(lista_tareas, archivo)

# Función para agregar una tarea a la lista


def agregar_tarea(tarea):
    lista_tareas.append({"tarea": tarea, "completada": False})

# Función para marcar una tarea como completada


def marcar_completada(numero):
    if 1 <= numero <= len(lista_tareas):
        lista_tareas[numero - 1]["completada"] = True
    else:
        print("Número de tarea inválido.")

# Función para limpiar la lista de tareas completadas


def limpiar_completadas():
    global lista_tareas
    lista_tareas = [tarea for tarea in lista_tareas if not tarea["completada"]]

# Función para ver elementos guardados


def ver_elementos_guardados():
    print("\n--- Elementos Guardados ---")
    for i, tarea in enumerate(lista_tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['tarea']} - {estado}")


# Cargar la lista de tareas al inicio del programa
lista_tareas = cargar_lista_tareas()

# Ciclo principal
while True:
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Actualizar elementos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        tarea = input("Ingresa una tarea: ")
        agregar_tarea(tarea)
        guardar_lista_tareas()  # Guardar automáticamente después de agregar
    elif opcion == '2':
        print("\nTareas pendientes:")
        for i, tarea in enumerate(lista_tareas, start=1):
            if not tarea["completada"]:
                print(f"{i}. {tarea['tarea']}")
        numero_tarea = int(input("Ingresa el número de la tarea completada: "))
        marcar_completada(numero_tarea)
        guardar_lista_tareas()  # Guardar automáticamente después de marcar como completada
    elif opcion == '3':
        ver_elementos_guardados()  # Mostrar elementos guardados
    elif opcion == '4':
        limpiar_completadas()  # Limpiar tareas completadas antes de salir
        guardar_lista_tareas()  # Guardar antes de salir
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

    # Mostrar la lista de elementos guardados después de cada operación
    ver_elementos_guardados()
