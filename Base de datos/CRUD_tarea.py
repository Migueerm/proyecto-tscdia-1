import mysql.connector

# Configuración de la conexión
config = {
    'user': 'root',
    'password': 'Noah2016',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'edutareas'
}

def obtener_conexion():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# CRUD para tabla tarea
def crear_tarea(Titulo, Prioridad, Descripcion, Fecha_Entrega, Estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO tarea (Titulo, Prioridad, Descripcion, Fecha_Entrega, Estado) VALUES (%s, %s, %s, %s, %s)"
    valores = (Titulo, Prioridad, Descripcion, Fecha_Entrega, Estado)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Tarea creada correctamente")

def leer_tareas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tarea")
    resultados = cursor.fetchall()
    if resultados:
        for tarea in resultados:
            print(tarea)
    else:
        print("No se encontraron tareas.")
    cursor.close()
    conexion.close()

def actualizar_tarea(ID_Tarea, Titulo=None, Prioridad=None, Descripcion=None, Fecha_Entrega=None, Estado=None):
    if None in (ID_Tarea, Titulo, Prioridad, Fecha_Entrega, Estado):
        print("Todos los campos son requeridos")
        return
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE tarea SET Titulo=%s, Prioridad=%s, Descripcion=%s, Fecha_Entrega=%s, Estado=%s WHERE ID_Tarea=%s"
    valores = (Titulo, Prioridad, Descripcion, Fecha_Entrega, Estado, ID_Tarea)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Tarea {ID_Tarea} actualizada correctamente")

def borrar_tarea(ID_Tarea):
    if ID_Tarea is None:
        print("ID de tarea es requerido")
        return
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM tarea WHERE ID_Tarea=%s"
    valores = (ID_Tarea,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Tarea {ID_Tarea} eliminada correctamente")

def mostrar_menu_tareas():
    print("\nMenú de Tareas:")
    print("1. Crear tarea")
    print("2. Leer tareas")
    print("3. Actualizar tarea")
    print("4. Borrar tarea")
    print("0. Salir")

def ejecutar_opcion_tareas(opcion):
    if opcion == 1:
        Titulo = input("Título: ")
        Prioridad = input("Prioridad: ")
        Descripcion = input("Descripción: ")
        Fecha_Entrega = input("Fecha de Entrega (YYYY-MM-DD): ")
        Estado = input("Estado: ")
        crear_tarea(Titulo, Prioridad, Descripcion, Fecha_Entrega, Estado)
    elif opcion == 2:
        leer_tareas()
    elif opcion == 3:
        ID_Tarea = input("ID Tarea: ")
        Titulo = input("Nuevo Título: ")
        Prioridad = input("Nueva Prioridad : ")
        Descripcion = input("Nueva Descripción : ")
        Fecha_Entrega = input("Nueva Fecha de Entrega (YYYY-MM-DD): ")
        Estado = input("Nuevo Estado: ")
        actualizar_tarea(ID_Tarea, Titulo or None, Prioridad or None, Descripcion or None, Fecha_Entrega or None, Estado or None)
    elif opcion == 4:
        ID_Tarea = input("ID Tarea: ")
        borrar_tarea(ID_Tarea)
    elif opcion == 0:
        print("Saliendo del programa de tareas...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_tareas():
    while True:
        mostrar_menu_tareas()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_tareas(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_tareas()
