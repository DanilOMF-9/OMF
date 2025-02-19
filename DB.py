import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Вычисление суммы возрасов пользователей
cursor.execute("SELECT SUM(age) FROM Users")
total_age = cursor.fetchone()[0]

print("Общее количество пользователей:", total_age)
connection.close()


