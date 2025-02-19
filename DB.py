import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Нахождения максимума возрата
cursor.execute("SELECT MAX(age) FROM Users")
max_age = cursor.fetchone()[0]

print("Минимум ввозрост пользователей:", max_age)
connection.close()


