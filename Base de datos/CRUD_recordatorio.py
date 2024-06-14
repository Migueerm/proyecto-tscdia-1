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

# CRUD para tabla recordatorio
def crear_recordatorio(Mensaje, Fecha, Hora, Descripcion, ID_Tarea):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO recordatorio (Mensaje, Fecha, Hora, Descripcion, ID_Tarea) VALUES (%s, %s, %s, %s, %s)"
    valores = (Mensaje, Fecha, Hora, Descripcion, ID_Tarea)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Recordatorio creado correctamente")

def leer_recordatorios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM recordatorio")
    resultados = cursor.fetchall()
    if resultados:
        for recordatorio in resultados:
            print(recordatorio)
    else:
        print("No se encontraron recordatorios.")
    cursor.close()
    conexion.close()
    print("Lectura de recordatorios realizada correctamente")

def actualizar_recordatorio(ID_Recordatorio, Mensaje=None, Fecha=None, Hora=None, Descripcion=None, ID_Tarea=None):
    if None in (ID_Recordatorio, Mensaje, Fecha, Hora, Descripcion, ID_Tarea):
        print("Todos los campos son requeridos")
        return
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE recordatorio SET Mensaje=%s, Fecha=%s, Hora=%s, Descripcion=%s, ID_Tarea=%s WHERE ID_Recordatorio=%s"
    valores = (Mensaje, Fecha, Hora, Descripcion, ID_Tarea, ID_Recordatorio)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Recordatorio {ID_Recordatorio} actualizado correctamente")

def borrar_recordatorio(ID_Recordatorio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM recordatorio WHERE ID_Recordatorio=%s"
    valores = (ID_Recordatorio,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Recordatorio {ID_Recordatorio} eliminado correctamente")

def mostrar_menu_recordatorios():
    print("\nMenú de Recordatorios:")
    print("1. Crear recordatorio")
    print("2. Leer recordatorios")
    print("3. Actualizar recordatorio")
    print("4. Borrar recordatorio")
    print("0. Salir")

def ejecutar_opcion_recordatorios(opcion):
    if opcion == 1:
        Mensaje = input("Mensaje: ")
        Fecha = input("Fecha (YYYY-MM-DD): ")
        Hora = input("Hora (HH:mm): ")
        Descripcion = input("Descripción: ")
        ID_Tarea = input("ID Tarea: ")
        crear_recordatorio(Mensaje, Fecha, Hora, Descripcion, ID_Tarea)
    elif opcion == 2:
        leer_recordatorios()
    elif opcion == 3:
        ID_Recordatorio = input("ID Recordatorio: ")
        Mensaje = input("Nuevo Mensaje: ")
        Fecha = input("Nueva Fecha (YYYY-MM-DD): ")
        Hora = input("Nueva Hora (HH:mm): ")
        Descripcion = input("Nueva Descripción: ")
        ID_Tarea = input("Nuevo ID Tarea: ")
        actualizar_recordatorio(ID_Recordatorio, Mensaje or None, Fecha or None, Hora or None, Descripcion or None, ID_Tarea or None)
    elif opcion == 4:
        ID_Recordatorio = input("ID Recordatorio: ")
        borrar_recordatorio(ID_Recordatorio)
    elif opcion == 0:
        print("Saliendo del programa de recordatorios...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_recordatorios():
    while True:
        mostrar_menu_recordatorios()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_recordatorios(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_recordatorios()
