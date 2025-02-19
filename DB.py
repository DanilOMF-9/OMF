import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

#Вывод результата
for user in users:
    print(users)
#Сохранение изменения и закрытием соединение

connection.close()


