import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Добавлене нового пользователя
cursor.execute('UPDATE Users SET age = ? WHERE username = ?',(29, 'newuser'))

#Сохранение изменения и закрытием соединение
connection.commit()
connection.close()


