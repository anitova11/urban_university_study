import sqlite3

# connection = sqlite3.connect('database_admin_bot.db')
# cursor = connection.cursor()
# connection.commit()
# connection.close()


def initiate_db():
    connection = sqlite3.connect('database_admin_bot.db')
    cursor = connection.cursor()
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database_admin_bot.db')
    cursor = connection.cursor()
    all_products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    connection.close()
    return all_products


def is_included(username):
    connection = sqlite3.connect('database_admin_bot.db')
    cursor = connection.cursor()
    users = cursor.execute("SELECT * FROM Users").fetchall()
    bol = False
    for user in users:
        if username.lower() == user[1].lower():
            bol = True
    connection.commit()
    connection.close()
    return bol


def add_user(username, email, age):
    connection = sqlite3.connect('database_admin_bot.db')
    cursor = connection.cursor()
    if not is_included(username):
        cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()
    connection.close()
