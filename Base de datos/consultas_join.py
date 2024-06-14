#Consultas join
#Conectada a la base de datos "edutareas" 

import mysql.connector
from tabulate import tabulate
from db_config import get_db_connection

def obtener_conexion():
    config = {
        'user': 'root',
        'password': 'CONTRASEÑA',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'edutareas'
    }
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

#Esta funciona
#Corregida
def leer_datos_con_join_inscripcion_estudiante():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        sql = """
        SELECT inscripcion.ID_Estudiante, estudiante.Nombre_Apellido
        FROM inscripcion
        INNER JOIN estudiante ON inscripcion.ID_Estudiante = estudiante.ID_Estudiante
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(tabulate(resultados, headers=["ID_Estudiante", "Nombre y Apellido"], tablefmt="grid"))
        #Esto hace que los resultados se muestren en una tabla para que sea un poco más ordenado visualmente :)
    except mysql.connector.Error as err:
        print(f"Error al leer datos con JOIN: {err}")
    finally:
        cursor.close()
        conexion.close()

#Funcion que se implementa
leer_datos_con_join_inscripcion_estudiante()


#Corregida
#Lista los cursos con estudiantes inscriptos
def leer_datos_con_join_inscripcion_cursos():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        sql = """
        SELECT inscripcion.ID_Curso, curso.Nombre_Curso
        FROM inscripcion
        INNER JOIN curso ON inscripcion.ID_Curso = curso.ID_Curso
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(tabulate(resultados, headers=["ID_Curso", "Nombre Curso"], tablefmt="grid"))
    except mysql.connector.Error as err:
        print(f"Error al leer datos con JOIN: {err}")
    finally:
        cursor.close()
        conexion.close()

#Funcion que se implementa
leer_datos_con_join_inscripcion_cursos()


#Corregida
#Lista los profesores con cursos inscriptos
def leer_datos_con_join_nombre_profesor():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        sql = """
        SELECT curso_profesor.ID_Curso, profesor.Nombre_Apellido
        FROM curso_profesor
        INNER JOIN profesor ON curso_profesor.ID_Profesor = profesor.ID_Profesor
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(tabulate(resultados, headers=["ID Curso", "Nombre y Apellido Profesor"], tablefmt="grid"))
    except mysql.connector.Error as err:
        print(f"Error al leer datos con JOIN: {err}")
    finally:
        cursor.close()
        conexion.close()

#Funcion que se implementa
leer_datos_con_join_nombre_profesor()


#Corregida
#Lista las tareas asociadas a materias
def leer_datos_con_join_materias_con_tareas():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        sql = """
        SELECT tarea_materia.ID_Materia, tarea.Titulo
        FROM tarea_materia
        INNER JOIN tarea ON tarea_materia.ID_Tarea = tarea.ID_Tarea
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(tabulate(resultados, headers=["ID Materia", "Tarea"], tablefmt="grid"))
    except mysql.connector.Error as err:
        print(f"Error al leer datos con JOIN: {err}")
    finally:
        cursor.close()
        conexion.close()

#Funcion que se implementa
leer_datos_con_join_materias_con_tareas()


#Corregida
#Lista los mails para compartir
def leer_datos_con_join_mails():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        sql = """
        SELECT estudiante_compartir.ID_Estudiante, estudiante.Correo_electronico
        FROM estudiante
        INNER JOIN estudiante_compartir ON estudiante_compartir.ID_Estudiante = estudiante.ID_Estudiante
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(tabulate(resultados, headers=["ID Estudiante", "Email"], tablefmt="grid"))
    except mysql.connector.Error as err:
        print(f"Error al leer datos con JOIN: {err}")
    finally:
        cursor.close()
        conexion.close()

#Funcion que se implementa
leer_datos_con_join_mails()