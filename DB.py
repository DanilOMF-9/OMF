import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбираем всех  пользователей
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

for user in users:
    print(user)
    
connection.close()


