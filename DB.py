import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

#Преобразование результата в список словаря
users_list = []
for user in users:
    user_dict = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
users_list.append(user_dict)

#Вывод
for user in users_list:
    print(user)
    
connection.close()


