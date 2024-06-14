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

# CRUD para tabla curso_profesor
def crear_curso_profesor(ID_Curso, ID_Profesor, Año_academico, Semestre):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO curso_profesor (ID_Curso, ID_Profesor, Año_academico, Semestre) VALUES (%s, %s, %s, %s)"
    valores = (ID_Curso, ID_Profesor, Año_academico, Semestre)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso de profesor creado correctamente")

def leer_cursos_profesor():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM curso_profesor")
    resultados = cursor.fetchall()
    if resultados:
        for curso_profesor in resultados:
            print(curso_profesor)
    else:
        print("No se encontraron cursos de profesor.")
    cursor.close()
    conexion.close()
    print("Lectura de cursos de profesor realizada correctamente")

def actualizar_curso_profesor(ID_Curso, ID_Profesor=None, Año_academico=None, Semestre=None):
    # Verificar que todos los campos estén presentes
    if None in (ID_Curso, ID_Profesor, Año_academico, Semestre):
        print("Todos los campos son requeridos")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE curso_profesor SET ID_Profesor=%s, Año_academico=%s, Semestre=%s WHERE ID_Curso=%s"
    valores = (ID_Profesor, Año_academico, Semestre, ID_Curso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso de profesor actualizado correctamente")

def borrar_curso_profesor(ID_Curso):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM curso_profesor WHERE ID_Curso=%s"
    valores = (ID_Curso,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Curso de profesor borrado correctamente")

def mostrar_menu_cursos_profesor():
    print("\nMenú de Cursos de Profesor:")
    print("1. Crear curso de profesor")
    print("2. Leer cursos de profesor")
    print("3. Actualizar curso de profesor")
    print("4. Borrar curso de profesor")
    print("0. Salir")

def ejecutar_opcion_cursos_profesor(opcion):
    if opcion == 1:
        ID_Curso = input("ID Curso: ")
        ID_Profesor = input("ID Profesor: ")
        Año_academico = input("Año Académico: ")
        Semestre = input("Semestre: ")
        crear_curso_profesor(ID_Curso, ID_Profesor, Año_academico, Semestre)
    elif opcion == 2:
        leer_cursos_profesor()
    elif opcion == 3:
        ID_Curso = input("ID Curso: ")
        ID_Profesor = input("Nuevo ID Profesor: ")
        Año_academico = input("Nuevo Año Académico: ")
        Semestre = input("Nuevo Semestre: ")
        actualizar_curso_profesor(ID_Curso, ID_Profesor or None, Año_academico or None, Semestre or None)
    elif opcion == 4:
        ID_Curso = input("ID Curso: ")
        borrar_curso_profesor(ID_Curso)
    elif opcion == 0:
        print("Saliendo del programa de cursos de profesor...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_cursos_profesor():
    while True:
        mostrar_menu_cursos_profesor()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_cursos_profesor(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_cursos_profesor()

