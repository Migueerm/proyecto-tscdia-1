# db_config.py

def get_db_connection():
    import mysql.connector
    return mysql.connector.connect(
        host="3306",
        user="root",
        password="Aasx76tcy_159",
        database="edutareas"
    )
