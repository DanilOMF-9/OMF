import sqlite3

#Установка соединенияч с базой 
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

try:
    #нАЧ ТРАНЗАКЦИИ
    cursor.execute('BEGIN')

    #вЫПОЛНЯЕМ ОПЕРАЦИИ
    cursor.execute('INSERT INTO Users(username, email) VALUES (?, ?)', ('user1','user1@example.com'))
    cusror.execute('INSERT INTO Users(username, email) VALUES (?, ?)', ('user2','user2@example.com'))

    #Подтверждаем изменения
    cursor.execute('COMMIT')

except:
    #Отменяем транзакции в случае ошибки
    cursor.execute('ROLLBACK'

                   )
connection.close()


