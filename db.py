import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Karlen-1999',
    database='contactos'
)

def rellenar_datos(nom, email, ident, area):
    q = f"""INSERT INTO contactos (Nombre, Email, ident, area) 
            VALUES ('{nom}', '{email}', '{ident}', '{area}')"""
    cursor = db.cursor()
    cursor.execute(q)
    db.commit()

def cerrar_conexion():
    db.close()
