import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Нахождения минимум возрата
cursor.execute("SELECT MIN(age) FROM Users")
min_age = cursor.fetchone()[0]

print("Минимум ввозрост пользователей:", min_age)
connection.close()


