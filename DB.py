import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Нахождение пользователей с наибольшим возростом
cursor.execute('''
SELECT username, age
FROM Users
WHERE age =(SELECT MAX(age) FROM Users)
''')
oldest_users = cursor.fetchall()

for user in oldest_users:
    print(user)
    
connection.close()


