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

# CRUD para tabla calendario
def crear_calendario(ID_Calendario, Tipo, Fecha, ID_Profesor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO calendario (ID_Calendario, Tipo, Fecha, ID_Profesor) VALUES (%s, %s, %s, %s)"
    valores = (ID_Calendario, Tipo, Fecha, ID_Profesor)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Calendario creado correctamente")

def leer_calendarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM calendario")
    resultados = cursor.fetchall()
    if resultados:
        for calendario in resultados:
            print(calendario)
    else:
        print("No se encontraron calendarios.")
    cursor.close()
    conexion.close()
    print("Lectura de calendarios realizada correctamente")

def actualizar_calendario(ID_Calendario, Tipo=None, Fecha=None, ID_Profesor=None):
    # Verificar que todos los campos estén presentes
    if None in (ID_Calendario, Tipo, Fecha):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE calendario SET Tipo=%s, Fecha=%s, ID_Profesor=%s WHERE ID_Calendario=%s"
    valores = (Tipo, Fecha, ID_Profesor, ID_Calendario)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Calendario actualizado correctamente")

def borrar_calendario(ID_Calendario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM calendario WHERE ID_Calendario=%s"
    valores = (ID_Calendario,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Calendario borrado correctamente")

def mostrar_menu_calendarios():
    print("\nMenú de Calendarios:")
    print("1. Crear calendario")
    print("2. Leer calendarios")
    print("3. Actualizar calendario")
    print("4. Borrar calendario")
    print("0. Salir")

def ejecutar_opcion_calendarios(opcion):
    if opcion == 1:
        ID_Calendario = input("ID Calendario: ")
        Tipo = input("Tipo: ")
        Fecha = input("Fecha (YYYY-MM-DD): ")
        ID_Profesor = input("ID Profesor: ")
        crear_calendario(ID_Calendario, Tipo, Fecha, ID_Profesor)
    elif opcion == 2:
        leer_calendarios()
    elif opcion == 3:
        ID_Calendario = input("ID Calendario: ")
        Tipo = input("Nuevo Tipo: ")
        Fecha = input("Nueva Fecha (YYYY-MM-DD): ")
        ID_Profesor = input("Nuevo ID Profesor: ")
        actualizar_calendario(ID_Calendario, Tipo or None, Fecha or None, ID_Profesor or None)
    elif opcion == 4:
        ID_Calendario = input("ID Calendario: ")
        borrar_calendario(ID_Calendario)
    elif opcion == 0:
        print("Saliendo del programa de calendarios...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_calendarios():
    while True:
        mostrar_menu_calendarios()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_calendarios(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_calendarios()
