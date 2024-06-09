Algoritmo BorradorGestorTareas
    Dimensionar tareas(100,3)
    Dimensionar categorias(20)
    Definir numTareas, numCategorias, opcion Como Entero
    Definir tarea, categoria, estado Como Cadena
    numTareas <- 0
    numCategorias <- 0
    Repetir
        Escribir '1. Agregar tarea'
        Escribir '2. Marcar tarea como completa'
        Escribir '3. Modificar estado de tarea'
        Escribir '4. Listar tareas'
        Escribir '5. Lista de categorías'
        Escribir '6. Salir'
        Escribir 'Ingrese una opción:'
        Leer opcion
        Según opcion Hacer
            1:
                Escribir 'Ingrese la tarea:'
                Leer tarea
                Escribir 'Ingrese la categoría:'
                Leer categoria
                numTareas <- numTareas+1
                tareas[numTareas,1] <- tarea
                tareas[numTareas,2] <- categoria
                tareas[numTareas,3] <- 'pendiente'
            2:
                Escribir 'Ingrese el número de tarea a marcar como completa:'
                Leer tarea
                tareas[tarea,3] <- 'completa'
            3:
                Escribir 'Ingrese el número de tarea a modificar:'
                Leer tarea
                Escribir 'Ingrese el nuevo estado (pendiente/completa):'
                Leer estado
                tareas[tarea,3] <- estado
            4:
                Para i <- 1 Hasta numTareas Hacer
                    Escribir i, '. ', tareas[i,1], ' (', tareas[i,2], ') - ', tareas[i,3]
                FinPara
            5:
                Para i <- 1 Hasta numCategorias Hacer
                    Escribir i, '. ', categorias[i]
                FinPara
            6:
                Escribir '¡Hasta luego!'
            De Otro Modo:
                Escribir 'Opción inválida'
        FinSegún
    Hasta Que opcion = 6
FinAlgoritmo
