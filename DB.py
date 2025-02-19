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

#Фильтрацич гкрппы по среднему возпросту больше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filtered_results = cursor.fetchall()

for row in filtered_results:
    print(row)
#Сохранение изменения и закрытием соединение

connection.close()


