import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Добавлене нового пользователя
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser',))

#Сохранение изменения и закрытием соединение
connection.commit()
connection.close()


