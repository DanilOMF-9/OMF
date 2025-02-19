import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#Создание таблици Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
''')

#сОЗДАНИЕ ТРИГИРРА ДЛЯ ОБНОВЛЕНИЯ ВРЕМЕНИ СОЗДАНИЯ ПР ИВСТАВКЕ НОВОЙ ЗВПИСИС
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS uptade_created_at
AFTER INSERT ON Users
BEGIN
UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE
id = NEW.id;
END;
''')

connection.commit()
connection.close()
