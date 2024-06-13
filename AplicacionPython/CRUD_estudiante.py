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

# CRUD para tabla estudiante
def crear_estudiante(id_estudiante, nombre_apellido, fecha_nacimiento, edad, correo_electronico, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO estudiante (ID_Estudiante, Nombre_Apellido, Fecha_Nacimiento, Edad, Correo_Electronico, Telefono) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (id_estudiante, nombre_apellido, fecha_nacimiento, edad, correo_electronico, telefono)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_estudiantes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante")
    resultados = cursor.fetchall()
    if resultados:
        for estudiante in resultados:
            print(estudiante)
    else:
        print("No se encontraron estudiantes.")
    cursor.close()
    conexion.close()

def actualizar_estudiante(ID_Estudiante, Nombre_Apellido=None, Fecha_nacimiento=None, Edad=None, Correo_electronico=None, Telefono=None):
    # Verificar que todos los campos estén presentes
    if None in (ID_Estudiante, Nombre_Apellido, Fecha_nacimiento, Edad, Correo_electronico, Telefono):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE estudiante SET Nombre_Apellido=%s, Fecha_Nacimiento=%s, Edad=%s, Correo_Electronico=%s, Telefono=%s WHERE ID_Estudiante=%s"
    valores = (Nombre_Apellido, Fecha_nacimiento, Edad, Correo_electronico, Telefono, ID_Estudiante)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()


def borrar_estudiante(ID_Estudiante):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM estudiante WHERE ID_Estudiante=%s"
    valores = (ID_Estudiante,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def mostrar_menu_estudiantes():
    print("\nMenú de Estudiantes:")
    print("1. Crear estudiante")
    print("2. Leer estudiantes")
    print("3. Actualizar estudiante")
    print("4. Borrar estudiante")
    print("0. Salir")

def ejecutar_opcion_estudiantes(opcion):
    if opcion == 1:
        ID_Estudiante = input("ID Estudiante: ")
        Nombre_Apellido = input("Nombre y Apellido: ")
        Fecha_Nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
        Edad = int(input("Edad: "))
        Correo_Electronico = input("Correo Electrónico: ")
        Telefono = input("Teléfono: ")
        crear_estudiante(ID_Estudiante, Nombre_Apellido, Fecha_Nacimiento, Edad, Correo_Electronico, Telefono)
    elif opcion == 2:
        leer_estudiantes()
    elif opcion == 3:
        ID_Estudiante = input("ID Estudiante: ")
        Nombre_Apellido = input("Nuevo Nombre y Apellido: ")
        fecha_nacimiento = input("Nueva Fecha de Nacimiento (YYYY-MM-DD): ")
        edad = input("Nueva Edad: ")
        correo_electronico = input("Nuevo Correo Electrónico: ")
        telefono = input("Nuevo Teléfono: ")
        actualizar_estudiante(ID_Estudiante, Nombre_Apellido or None, fecha_nacimiento or None, int(edad) if edad else None, correo_electronico or None, telefono or None)
    elif opcion == 4:
        id_estudiante = input("ID Estudiante: ")
        borrar_estudiante(id_estudiante)
    elif opcion == 0:
        print("Saliendo del programa de estudiantes...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_estudiantes():
    while True:
        mostrar_menu_estudiantes()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_estudiantes(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_estudiantes()

