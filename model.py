import mysql.connector
from flask import Flask
class Cliente:
    objetos = []

    def __init__(self, **kwargs):
        self.id = int(kwargs['id'])
        self.nombre = kwargs['nombre']
        self.email = kwargs['email']
        self.telefono = kwargs['telefono']
        self.direccion = kwargs['direccion']
        self.ciudad = kwargs['ciudad']
        self.pais = kwargs['pais']
        Cliente.objetos.append(self)

    def __repr__(self):
        return f'Cliente(id={repr(self.id)}, nombre={repr(self.nombre)}, email={repr(self.nombre)})'

    def __str__(self):
        return f'{self.nombre}, {self.id}'


def get_db_connection():
    # Replace 'your_database_name' with the name of your MariaDB database
    # Replace 'your_username' and 'your_password' with your database credentials
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='wan',
        password='0420',
        database='users'
    )
    return connection
def user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT nombre, direccion, ciudad, pais, telefono FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    # Make sure to handle the result and close the cursor and connection properly
    if result:
        nombre, direccion, ciudad, pais, telefono = result
    else:
        # Handle the case where the user is not found with the given user_id
        nombre, direccion, ciudad, pais, telefono = None, None, None, None, None

    cursor.close()
    connection.close()

    return user_id, nombre, direccion, ciudad, pais, telefono 


def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)

    users = cursor.fetchall()

    # Create a list to store Cliente instances
    clientes = []
    for user in users:
        cliente = Cliente(
            id=user[0],
            nombre=user[1],
            direccion=user[2],
            ciudad=user[3],
            pais=user[4],
            telefono=user[5],
            email=user[6],
        )
        clientes.append(cliente)

    cursor.close()
    connection.close()

    return clientes



def insert_user(nombre, direccion, ciudad, pais, telefono, email):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO users (nombre, direccion, ciudad, pais, telefono, email) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (nombre, direccion, ciudad, pais, telefono, email)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()

def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DELETE FROM users WHERE id=%s"
    data = (user_id,)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()

def update_user(user_id, nombre, direccion, ciudad, pais, telefono, email):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "UPDATE users SET nombre=%s, direccion=%s, ciudad=%s, pais=%s, telefono=%s, email=%s WHERE id=%s"
    data = (nombre, direccion, ciudad, pais, telefono, email, user_id)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()
