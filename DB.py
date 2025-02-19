import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбираем пользователей с неизвестным возростом
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknown_age_users = cursor.fetchall()

#Вывод
for user in unknown_age_users:
    print(user)

connection.close()


