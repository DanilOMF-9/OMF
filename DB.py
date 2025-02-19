import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Создаем представление для активных пользователей

cursor.execute('CREATE VIEW ActiveUsers AS SELECT * FROM Users WHERE is_active = 1')

#вВЫБИАРЕМ АКТИВНЫХ АОЛЬЗОВАТЕЛЕЙ
cursor.execute('SELECT * FROM ActiveUsers')
active_users = cursor.fetchall()

for user in active_users:
    print(user)

connection.close()

