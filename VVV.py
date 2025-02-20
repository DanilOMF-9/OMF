import sqlite3

connection = sqlite3.connect('TV.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Proisvod(
    id_proisvod INTEGER PRIMARY KEY,
    name_proisvod VARCHAR NOT NULL
)
''')

# Создание таблицы Клиенты (Customers)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers(
    id_client INTEGER PRIMARY KEY,
    fio VARCHAR NOT NULL
)
''')

# Создание таблицы Телевизоры (Tv)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tv(
    id_tv INTEGER PRIMARY KEY,
    id_proisvod INTEGER NOT NULL,
    model_name VARCHAR NOT NULL,
    diagonal_size INTEGER NOT NULL,
    price DECIMAL NOT NULL,
    discount DECIMAL NOT NULL,
    FOREIGN KEY (id_proisvod) REFERENCES Proisvod (id_proisvod)
)
''')

# Создание таблицы Клиент (Client)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    id_orders INTEGER PRIMARY KEY,
    id_client INTEGER NOT NULL,
    order_date DATE,
    location VARCHAR NOT NULL,
    skidka DECIMAL NOT NULL,
    FOREIGN KEY (id_client) REFERENCES Customers(id_client)
)
''')

# Создание таблицы Заказы_Телевизоры (Order_tv)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Order_tv(
    id_orders INTEGER NOT NULL,
    id_tv INTEGER NOT NULL,
    kolicestvo INTEGER NOT NULL,
    price_unit DECIMAL NOT NULL,
    skidka DECIMAL NOT NULL,
    PRIMARY KEY (id_orders, id_tv),
    FOREIGN KEY (id_orders) REFERENCES Client(id_orders),
    FOREIGN KEY (id_tv) REFERENCES Tv (id_tv)
)
''')

connection.commit()
connection.close()
