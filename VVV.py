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

# Заполнение таблицы Proisvod
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Samsung')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('LG')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Sony')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Philips')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('TCL')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Hisense')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Panasonic')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Sharp')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Vizio')")
cursor.execute("INSERT INTO Proisvod (name_proisvod) VALUES ('Xiaomi')")

# Заполнение таблицы Customers
cursor.execute("INSERT INTO Customers (fio) VALUES ('Иванов Иван Иванович')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Петров Петр Петрович')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Сидоров Сидор Сидорович')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Смирнов Алексей Андреевич')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Кузнецов Дмитрий Сергеевич')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Попова Елена Владимировна')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Васильева Ольга Ивановна')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Федоров Михаил Петрович')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Николаева Анна Юрьевна')")
cursor.execute("INSERT INTO Customers (fio) VALUES ('Андреев Сергей Викторович')")

# Заполнение таблицы Tv
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (1, 'Samsung QLED 55', 55, 800.00, 0.05)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (2, 'LG OLED 65', 65, 1200.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (3, 'Sony Bravia XR 55', 55, 900.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (4, 'Philips Ambilight 50', 50, 700.00, 0.10)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (5, 'TCL QLED 65', 65, 1000.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (6, 'Hisense ULED 55', 55, 650.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (7, 'Panasonic OLED 55', 55, 1100.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (8, 'Sharp Aquos 60', 60, 750.00, 0.00)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (9, 'Vizio OLED 65', 65, 950.00, 0.15)")
cursor.execute("INSERT INTO Tv (id_proisvod, model_name, diagonal_size, price, discount) VALUES (10, 'Xiaomi Mi TV 55', 55, 550.00, 0.00)")

# Заполнение таблицы Client
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (1, '2024-01-15', 'Москва', 0.00)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (2, '2024-01-20', 'Санкт-Петербург', 0.05)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (3, '2024-01-25', 'Казань', 0.00)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (4, '2024-02-01', 'Екатеринбург', 0.10)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (5, '2024-02-05', 'Новосибирск', 0.00)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (6, '2024-02-10', 'Нижний Новгород', 0.00)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (7, '2024-02-15', 'Самара', 0.05)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (8, '2024-02-20', 'Омск', 0.00)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (9, '2024-02-25', 'Челябинск', 0.10)")
cursor.execute("INSERT INTO Client (id_client, order_date, location, skidka) VALUES (10, '2024-03-01', 'Ростов-на-Дону', 0.00)")

# Заполнение таблицы Order_tv
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (1, 1, 1, 800.00, 0.05)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (2, 2, 1, 1200.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (3, 3, 1, 900.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (4, 4, 2, 700.00, 0.10)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (5, 5, 1, 1000.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (6, 6, 1, 650.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (7, 7, 1, 1100.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (8, 8, 1, 750.00, 0.00)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (9, 9, 1, 950.00, 0.15)")
cursor.execute("INSERT INTO Order_tv (id_orders, id_tv, kolicestvo, price_unit, skidka) VALUES (10, 10, 3, 550.00, 0.00)")


connection.commit()
connection.close()
