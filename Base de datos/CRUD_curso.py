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

# CRUD para tabla curso
def crear_curso(ID_Curso, Nombre_Curso, Descripcion_Curso):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO curso (ID_Curso, Nombre_Curso, Descripcion_Curso) VALUES (%s, %s, %s)"
    valores = (ID_Curso, Nombre_Curso, Descripcion_Curso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso creado correctamente")

def leer_cursos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM curso")
    resultados = cursor.fetchall()
    if resultados:
        for curso in resultados:
            print(curso)
    else:
        print("No se encontraron cursos.")
    cursor.close()
    conexion.close()
    print("Lectura de cursos realizada correctamente")

def actualizar_curso(ID_Curso, Nombre_Curso=None, Descripcion_Curso=None):
 # Verificar que todos los campos estén presentes
    if None in (ID_Curso, Nombre_Curso, Descripcion_Curso):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE curso SET Nombre_Curso=%s, Descripcion_Curso=%s WHERE ID_Curso=%s"
    valores = (Nombre_Curso, Descripcion_Curso, ID_Curso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso actualizado correctamente")

def borrar_curso(ID_Curso):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM curso WHERE ID_Curso=%s"
    valores = (ID_Curso,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso borrado correctamente")

def mostrar_menu_cursos():
    print("\nMenú de Cursos:")
    print("1. Crear curso")
    print("2. Leer cursos")
    print("3. Actualizar curso")
    print("4. Borrar curso")
    print("0. Salir")

def ejecutar_opcion_cursos(opcion):
    if opcion == 1:
        ID_Curso = input("ID Curso: ")
        Nombre_Curso = input("Nombre del Curso: ")
        Descripcion_Curso = input("Descripción del Curso: ")
        crear_curso(ID_Curso, Nombre_Curso, Descripcion_Curso)
    elif opcion == 2:
        leer_cursos()
    elif opcion == 3:
        ID_Curso = input("ID Curso: ")
        Nombre_Curso = input("Nuevo Nombre del Curso: ")
        Descripcion_Curso = input("Nueva Descripción del Curso: ")
        actualizar_curso(ID_Curso, Nombre_Curso or None, Descripcion_Curso or None)
    elif opcion == 4:
        ID_Curso = input("ID Curso: ")
        borrar_curso(ID_Curso)
    elif opcion == 0:
        print("Saliendo del programa de cursos...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_cursos():
    while True:
        mostrar_menu_cursos()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_cursos(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_cursos()