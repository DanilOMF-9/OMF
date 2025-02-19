import sqlite3

#Создание подключения к базе
connection = sqlite3.connect('my_database.db')
connection.close()
