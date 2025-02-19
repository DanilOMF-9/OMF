import sqlite3

#уСТАНАВЛДИВАЕМ СОЕДИНЕНИЕ С БД
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    try:
        #Начинаем танзакции автоматически
        with connection:
            #Выполныем операцию
            cursor.execute('INSERT INTO Users(username, emaiol) VALUES(?, ?)', ('user3', 'user3@example.com'))
            cursor.execute('INSERT INTO Users(username, emaiol) VALUES(?, ?)', ('user4', 'user4@example.com'))

    except:
        #Ошибка будет приводить к автоматическому отказу транзакции
        pass
            


