
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

### MODULO 2
