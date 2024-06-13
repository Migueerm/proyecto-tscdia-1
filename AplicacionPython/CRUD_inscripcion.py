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

# CRUD para tabla inscripcion
def crear_inscripcion(ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO inscripcion (ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final) VALUES (%s, %s, %s, %s)"
    valores = (ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Inscripción creada correctamente")

def leer_inscripciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM inscripcion")
    resultados = cursor.fetchall()
    if resultados:
        for inscripcion in resultados:
            print(inscripcion)
    else:
        print("No se encontraron inscripciones.")
    cursor.close()
    conexion.close()
    print("Lectura de inscripciones realizada correctamente")

def actualizar_inscripcion(ID_Estudiante, ID_Curso, Fecha_Inscripcion=None, Nota_Final=None):
    # Verificar que todos los campos estén presentes
    if None in (ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE inscripcion SET Fecha_Inscripcion=%s, Nota_Final=%s WHERE ID_Estudiante=%s AND ID_Curso=%s"
    valores = (Fecha_Inscripcion, Nota_Final, ID_Estudiante, ID_Curso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Inscripción actualizada correctamente")

def borrar_inscripcion(ID_Estudiante, ID_Curso):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM inscripcion WHERE ID_Estudiante=%s AND ID_Curso=%s"
    valores = (ID_Estudiante, ID_Curso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Inscripción borrada correctamente")

def mostrar_menu_inscripciones():
    print("\nMenú de Inscripciones:")
    print("1. Crear inscripción")
    print("2. Leer inscripciones")
    print("3. Actualizar inscripción")
    print("4. Borrar inscripción")
    print("0. Salir")

def ejecutar_opcion_inscripciones(opcion):
    if opcion == 1:
        ID_Estudiante = input("ID Estudiante: ")
        ID_Curso = input("ID Curso: ")
        Fecha_Inscripcion = input("Fecha de Inscripción (YYYY-MM-DD): ")
        Nota_Final = input("Nota Final: ")
        crear_inscripcion(ID_Estudiante, ID_Curso, Fecha_Inscripcion, Nota_Final)
    elif opcion == 2:
        leer_inscripciones()
    elif opcion == 3:
        ID_Estudiante = input("ID Estudiante: ")
        ID_Curso = input("ID Curso: ")
        Fecha_Inscripcion = input("Nueva Fecha de Inscripción (YYYY-MM-DD): ")
        Nota_Final = input("Nueva Nota Final: ")
        actualizar_inscripcion(ID_Estudiante, ID_Curso, Fecha_Inscripcion or None, Nota_Final or None)
    elif opcion == 4:
        ID_Estudiante = input("ID Estudiante: ")
        ID_Curso = input("ID Curso: ")
        borrar_inscripcion(ID_Estudiante, ID_Curso)
    elif opcion == 0:
        print("Saliendo del programa de inscripciones...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_inscripciones():
    while True:
        mostrar_menu_inscripciones()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_inscripciones(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_inscripciones()
