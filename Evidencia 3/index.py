
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
               tareas.modificar_tarea()
            elif opcion == "4":
                tareas.eliminar_tarea()
            elif opcion == "5":
                categorias.ingreso_categoria()
            elif opcion == "6":
                categorias.listar_categoria()
            elif opcion == "7":
                categorias.modificar_categoria()
            elif opcion == "8":
                categorias.eliminar_categoria()
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario. Saliendo del programa...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()

### MODULO 2




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

