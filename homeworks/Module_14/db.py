import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("test_user0", "ex0@gmail.com", "24"))
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"test_user{i}", f"ex{i}@gmail.com",
#     f"{24+i}"))

# cursor.execute("UPDATE Users SET age = ? WHERE username =  ?", (25, 'test_user'))

# cursor.execute("DELETE FROM Users WHERE username = ?", ("test_user0", ))

# cursor.execute('SELECT username, age, AVG(age) FROM Users WHERE age % 2 > 0 GROUP BY age')
cursor.execute('SELECT COUNT(*) FROM Users')
users = cursor.fetchall()
print(users)
# for user in users:
#     print(user)

connection.commit()
connection.close()
