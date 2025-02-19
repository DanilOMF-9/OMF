import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Получение средний возрост пользователя для каждого возроста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()

#Вывод
for row in results:
    print(row)

#Выбираем и сортируем пользователей по возросту по убыванию
cursor.execute('SELECT username, age FROM Users ORDER BY age DESC')
results = cursor.fetchall()

for row in results:
    print(row)
#Сохранение изменения и закрытием соединение

connection.close()


