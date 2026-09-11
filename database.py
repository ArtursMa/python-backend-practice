import sqlite3


def get_connection():
    return sqlite3.connect("beauty.db")


def get_all_clients():  
    beauty_database_connection = get_connection()
    clients_cursor = beauty_database_connection.execute("SELECT * FROM clients")
    all_clients_data = clients_cursor.fetchall()
    beauty_database_connection.close()
    return all_clients_data


def get_client_by_id(client_id):
    db_connection = get_connection()
    clients_cursor = db_connection.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    client_data = clients_cursor.fetchone()
    db_connection.close()
    return client_data


def add_client(name, phone, status):
    connection = get_connection()
    with connection:
        connection.execute("INSERT INTO clients(name,phone,status) VALUES(?,?,?)", (name, phone, status))
    connection.close()


add_client("Kate", "34343", 1)
