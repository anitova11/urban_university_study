import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute(f'INSERT INTO Users (username, email, age, balance) '
#                    f'VALUES ("User{i}", "example{i}@gmail.com", "{10*i}", 1000)'),
#
# cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 > 0")

# cursor.execute("DELETE FROM Users WHERE id % 3 == 1")

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
users = cursor.fetchall()
for i in users:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

connection.commit()
connection.close()
