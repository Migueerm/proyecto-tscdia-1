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

# CRUD para tabla profesor
def crear_profesor(ID_Profesor, Nombre_Apellido, Correo_electronico):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (ID_Profesor, Nombre_Apellido, Correo_electronico) VALUES (%s, %s, %s)"
    valores = (ID_Profesor, Nombre_Apellido, Correo_electronico)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Profesor {ID_Profesor} creado correctamente")

def leer_profesores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    resultados = cursor.fetchall()
    if resultados:
        for profesor in resultados:
            print(profesor)
    else:
        print("No se encontraron profesores.")
    cursor.close()
    conexion.close()
    print("Lectura de profesores realizada correctamente")

def actualizar_profesor(ID_Profesor, Nombre_Apellido=None, Correo_electronico=None):
    if None in (ID_Profesor, Nombre_Apellido, Correo_electronico):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET Nombre_Apellido=%s, Correo_electronico=%s WHERE ID_Profesor=%s"
    valores = (Nombre_Apellido, Correo_electronico, ID_Profesor)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Profesor {ID_Profesor} actualizado correctamente")

def borrar_profesor(ID_Profesor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE ID_Profesor=%s"
    valores = (ID_Profesor,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Profesor {ID_Profesor} eliminado correctamente")

def mostrar_menu_profesores():
    print("\nMenú de Profesores:")
    print("1. Crear profesor")
    print("2. Leer profesores")
    print("3. Actualizar profesor")
    print("4. Borrar profesor")
    print("0. Salir")

def ejecutar_opcion_profesores(opcion):
    if opcion == 1:
        ID_Profesor = input("ID Profesor: ")
        Nombre_Apellido = input("Nombre y Apellido: ")
        Correo_electronico = input("Correo electrónico: ")
        crear_profesor(ID_Profesor, Nombre_Apellido, Correo_electronico)
    elif opcion == 2:
        leer_profesores()
    elif opcion == 3:
        ID_Profesor = input("ID Profesor: ")
        Nombre_Apellido = input("Nuevo Nombre y Apellido: ")
        Correo_electronico = input("Nuevo Correo Electrónico: ")
        actualizar_profesor(ID_Profesor, Nombre_Apellido or None, Correo_electronico or None)
    elif opcion == 4:
        ID_Profesor = input("ID Profesor: ")
        borrar_profesor(ID_Profesor)
    elif opcion == 0:
        print("Saliendo del programa de profesores...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_profesores():
    while True:
        mostrar_menu_profesores()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_profesores(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_profesores()

