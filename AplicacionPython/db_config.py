# db_config.py
#usar para conectar a la base de datos. La contraseña debe ser reemplazadas :)

def get_db_connection():
    import mysql.connector
    return mysql.connector.connect(
        host="3306",
        user="root",
        password="CONTRASEÑA",
        database="edutareas"
    )
