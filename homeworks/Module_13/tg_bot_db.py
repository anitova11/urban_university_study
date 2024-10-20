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

# cursor.execute("DELETE FROM Users WHERE id == 6")

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
# users = cursor.fetchall()
# for i in users:
#     print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

cursor.execute("SELECT COUNT(*) FROM Users")
users_count = cursor.fetchall()[0][0]
cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchall()[0][0]
print(balance_sum/users_count)

connection.commit()
connection.close()
