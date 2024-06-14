import mysql.connector

# Configuración de la conexión
config = {
    'user': 'root',
    'password': 'Noah2016',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'edutareas'
}

# Lista de días válidos
DIAS_VALIDOS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

def obtener_conexion():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# CRUD para tabla materia
def crear_materia(Nombre, ID_Profesor, Ubicacion, Dias, Horario):
    if Dias.lower() not in DIAS_VALIDOS:
        print(f"Error: '{Dias}' no es un día válido. Use uno de {', '.join(DIAS_VALIDOS)}.")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO materia (Nombre, ID_Profesor, Ubicacion, Dias, Horario) VALUES (%s, %s, %s, %s, %s)"
    valores = (Nombre, ID_Profesor, Ubicacion, Dias, Horario)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Materia creada correctamente")

def leer_materias():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM materia")
    resultados = cursor.fetchall()
    if resultados:
        for materia in resultados:
            print(materia)
    else:
        print("No se encontraron materias.")
    cursor.close()
    conexion.close()
    print("Lectura de materias realizada correctamente")

def actualizar_materia(ID_Materia, Nombre=None, ID_Profesor=None, Ubicacion=None, Dias=None, Horario=None):
    # Verificar que ID_Materia esté presente
    if ID_Materia is None:
        print("ID de materia es requerido")
        return
    
    # Verificar si los días son válidos
    if Dias and Dias.lower() not in DIAS_VALIDOS:
        print(f"Error: '{Dias}' no es un día válido. Use uno de {', '.join(DIAS_VALIDOS)}.")
        return

    # Construir la lista de valores a actualizar
    valores = []
    if Nombre is not None:
        valores.append(f"Nombre = '{Nombre}'")
    if ID_Profesor is not None:
        valores.append(f"ID_Profesor = '{ID_Profesor}'")
    if Ubicacion is not None:
        valores.append(f"Ubicacion = '{Ubicacion}'")
    if Dias is not None:
        valores.append(f"Dias = '{Dias}'")
    if Horario is not None:
        valores.append(f"Horario = '{Horario}'")

    # Verificar que al menos un campo adicional a ID_Materia se vaya a actualizar
    if not valores:
        print("Nada que actualizar. Proporcione al menos un campo adicional a ID_Materia.")
        return

    # Construir y ejecutar la consulta SQL de actualización
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = f"UPDATE materia SET {', '.join(valores)} WHERE ID_Materia = {ID_Materia}"
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Materia actualizada correctamente")

def borrar_materia(ID_Materia):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM materia WHERE ID_Materia = %s"
    valores = (ID_Materia,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Materia borrada correctamente")

def mostrar_menu_materias():
    print("\nMenú de Materias:")
    print("1. Crear materia")
    print("2. Leer materias")
    print("3. Actualizar materia")
    print("4. Borrar materia")
    print("0. Salir")

def ejecutar_opcion_materias(opcion):
    if opcion == 1:
        Nombre = input("Nombre: ")
        ID_Profesor = input("ID Profesor: ")
        Ubicacion = input("Ubicación: ")
        Dias = input("Días (lunes, martes, miércoles, jueves, viernes, sábado): ")
        Horario = input("Horario: ")
        crear_materia(Nombre, ID_Profesor, Ubicacion, Dias, Horario)
    elif opcion == 2:
        leer_materias()
    elif opcion == 3:
        ID_Materia = input("ID Materia: ")
        Nombre = input("Nuevo Nombre: ")
        ID_Profesor = input("Nuevo ID Profesor: ")
        Ubicacion = input("Nueva Ubicación: ")
        Dias = input("Nuevos Días (lunes, martes, miércoles, jueves, viernes, sábado): ")
        Horario = input("Nuevo Horario: ")
        actualizar_materia(ID_Materia, Nombre, ID_Profesor, Ubicacion, Dias, Horario)
    elif opcion == 4:
        ID_Materia = input("ID Materia: ")
        borrar_materia(ID_Materia)
    elif opcion == 0:
        print("Saliendo del programa de materias...")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

def main_materias():
    while True:
        mostrar_menu_materias()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                break
            ejecutar_opcion_materias(opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main_materias()

