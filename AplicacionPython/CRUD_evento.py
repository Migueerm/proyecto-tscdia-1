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

# CRUD para tabla evento
def crear_evento(ID_Evento, Fecha, ID_Calendario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO evento (ID_Evento, Fecha, ID_Calendario) VALUES (%s, %s, %s)"
    valores = (ID_Evento, Fecha, ID_Calendario)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Evento creado correctamente")

def leer_eventos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM evento")
    resultados = cursor.fetchall()
    if resultados:
        for evento in resultados:
            print(evento)
    else:
        print("No se encontraron eventos.")
    cursor.close()
    conexion.close()
    print("Lectura de eventos realizada correctamente")

def actualizar_evento(ID_Evento, Fecha=None, ID_Calendario=None):
    # Verificar que todos los campos estén presentes
    if None in (ID_Evento, Fecha, ID_Calendario):
        print("Todos los campos son requeridos")
        return
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE evento SET Fecha=%s, ID_Calendario=%s WHERE ID_Evento=%s"
    valores = (Fecha, ID_Calendario, ID_Evento)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Evento actualizado correctamente")

def borrar_evento(ID_Evento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM evento WHERE ID_Evento=%s"
    valores = (ID_Evento,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Evento borrado correctamente")

def mostrar_menu_eventos():
    print("\nMenú de Eventos:")
    print("1. Crear evento")
    print("2. Leer eventos")
    print("3. Actualizar evento")
    print("4. Borrar evento")
    print("0. Salir")

def ejecutar_opcion_eventos(opcion):
    if opcion == 1:
        ID_Evento = input("ID Evento: ")
        Fecha = input("Fecha (YYYY-MM-DD): ")
        ID_Calendario = input("ID Calendario: ")
        crear_evento(ID_Evento, Fecha, ID_Calendario)
    elif opcion == 2:
        leer_eventos()
    elif opcion == 3:
        ID_Evento = input("ID Evento: ")
        Fecha = input("Nueva Fecha (YYYY-MM-DD): ")
        ID_Calendario = input("Nuevo ID Calendario: ")
        actualizar_evento(ID_Evento, Fecha or None, ID_Calendario or None)
    elif opcion == 4:
        ID_Evento = input("ID Evento: ")
        borrar_evento(ID_Evento)
    elif opcion == 0:
        print("Saliendo del programa de eventos...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_eventos():
    while True:
        mostrar_menu_eventos()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_eventos(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_eventos()
