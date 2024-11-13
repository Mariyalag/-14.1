import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

cursor.execute("DELETE FROM Users")

for i in range(1, 11):
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# cursor.execute("SELECT username, email, age, balance FROM Users")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()