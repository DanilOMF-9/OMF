import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#вЫБИРАЕМ ИМНА И ВОЗВРАЩАЕМ ПОЛЬЗОВАТЕЛЕЙ СТАРШЕ 25 ЛЕТ
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()

#Вывод
for row in results:
    print(row)

#Сохранение изменения и закрытием соединение

connection.close()


