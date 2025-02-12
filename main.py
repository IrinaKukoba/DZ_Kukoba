import sqlite3


def create_database():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        phone TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(id)
    )
    ''')

    conn.commit()
    conn.close()


def add_client(first_name, last_name, email):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO clients (first_name, last_name, email) VALUES (?, ?, ?)
    ''', (first_name, last_name, email))

    conn.commit()
    conn.close()


def add_phone(client_id, phone):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO phones (client_id, phone) VALUES (?, ?)
    ''', (client_id, phone))

    conn.commit()
    conn.close()


def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    if first_name:
        cursor.execute('UPDATE clients SET first_name = ? WHERE id = ?', (first_name, client_id))
    if last_name:
        cursor.execute('UPDATE clients SET last_name = ? WHERE id = ?', (last_name, client_id))
    if email:
        cursor.execute('UPDATE clients SET email = ? WHERE id = ?', (email, client_id))

    conn.commit()
    conn.close()


def delete_phone(phone_id):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM phones WHERE id = ?', (phone_id,))

    conn.commit()
    conn.close()


def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM phones WHERE client_id = ?', (client_id,))
    cursor.execute('DELETE FROM clients WHERE id = ?', (client_id,))

    conn.commit()
    conn.close()


def find_client(search_term):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM clients WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

    clients = cursor.fetchall()
    conn.close()
    return clients



if __name__ == '__main__':
    create_database()

    # Добавление клиентов
    add_client('Иван', 'Иванов', 'ivanov@example.com')
    add_client('Петр', 'Петров', 'petrov@example.com')

    # Добавление телефонов
    add_phone(1, '123-456-7890')
    add_phone(1, '098-765-4321')
    add_phone(2, '234-567-8901')

    # Изменение данных о клиенте
    update_client(1, email='new_ivanov@example.com')

    # Удаление телефона
    delete_phone(1)  # Например, удаляем номер '123-456-7890'

    # Удаление клиента
    delete_client(2)  # Удаляем клиента с ID 2

    # Поиск клиента
    clients_found = find_client('Иван')
    print(clients_found)  # Вывод информации о найденных клиентах
