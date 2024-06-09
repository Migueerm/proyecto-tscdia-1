
import tareas
import categorias

##MODULO 1 INTEGRANTES FLORENCIA Y MIGUEL
def mostrar_bienvenida():
    print("¡Bienvenido a la aplicación de gestión de tareas!")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingreso de tarea")
    print("2. Listar tareas")
    print("3. Modificar tarea")
    print("4. Eliminar tarea")
    print("5. Ingreso de categoría")
    print("6. Listar categorías")
    print("7. Modificar categoría")
    print("8. Eliminar categoría")
    print("0. Salir")

def main():
    mostrar_bienvenida()
    while True:
        try:
            mostrar_menu()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                tareas.ingreso_tarea()
            elif opcion == "2":
                tareas.listar_tareas()
            elif opcion == "3":

              ############### FLOR CONTINUAR #########################

### MODULO 2 INTEGRANTES GUADALUPE MENDOZA MELANIA

lista_categoria=[]
def ingreso_cateogoria():
    nombre_categoria= input("ingrese el nombre de la categoria: ")
    if nombre_categoria not in lista_categoria:
         lista_categoria.append(nombre_categoria)
         print (f"Categoría '{nomrbre_categoria}'añadida. ")
    else:
         print (f"La categoría'{nombre_categoria}' ya existe" )


import categorias
lista_tareas = []
def ingreso_tarea():
    categoria = input("Ingrese la categoría de la tarea: ")
    if categoria not in lista_categorias:
        crear_categoria = input("La categoría no existe. ¿Desea crearla? (si/no): ")
        if crear_categoria.lower() == "si":
            lista_categorias.append(categoria)
            print(f"Categoría '{categoria}' creada.")
        else:
            print("No se creó la categoría.")
            return
        descripcion= input("ingrese la descripción de la tarea")
    id_tarea = len(lista_tareas) + 1
    tarea = { 'id': id_tarea,
             'descripcion':descripcion,
            'estado': 'pendiente',
             'categoría':categoria }
    lista_tareas.append(tarea)
    print ("Tarea añadida con exito")

def  marcar_tarea_completa():
    id_tarea = int(input("Ingrese el ID de la tarea a marcar como completa: "))
    for tarea in lista_tareas:
        if tarea['id'] == id_tarea:
            tarea['estado'] = 'completa'
            print("Tarea marcada como completa.")
            return
    print("Tarea no encontrada.")


lista_tareas = []

def modificar_estado_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea: "))
    
    tarea = next((t for t in lista_tareas if t['id'] == id_tarea), None)
    
    if tarea:
        # Mostrar opciones de estado
        print("Seleccione el nuevo estado de la tarea:")
        print("1. Pendiente")
        print("2. Realizada")
        print("3. Observada")
        
        opcion_estado = input("Ingrese el número correspondiente al nuevo estado: ")
        estados = {"1": "Pendiente", "2": "Realizada", "3": "Observada"}
        
        if opcion_estado in estados:
            # Actualizar el estado de la tarea
            tarea['estado'] = estados[opcion_estado]
            print(f"El estado de la tarea con ID {id_tarea} ha sido actualizado a {tarea['estado']}.")
        else:
            print("Opción de estado no válida.")
    else:
        print("Tarea no encontrada.")

def listar_tareas():
    if not lista_tareas:
        print("No hay tareas para mostrar.")
    else:
        print("\nListado de Tareas:")
        for tarea in lista_tareas:
            print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}, Categoría: {tarea['categoria']}")

