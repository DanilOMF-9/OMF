import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Создаем индекс для столба "email"
cursor.execute('CREATE INDEX idx_email ON Users(email)')

#Сохранение изменения и закрытием соединение
connection.commit()
connection.close()


