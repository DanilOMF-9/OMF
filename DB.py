import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Получение средний возрост пользователя для каждого возроста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()

#Выбираем и сортируем пользователей по возрасту по убыванию
cursor.execute('''
SELECT username, age, AVG(age)
FROM Users
GROUP BY age
HAVING AVG(age)>?
ORDER BY age DESC
''', (30,))
results = cursor.fetchall()

for row in results:
    print(row)
#Сохранение изменения и закрытием соединение

connection.close()


