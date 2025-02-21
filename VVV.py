import sqlite3

connection = sqlite3.connect('TV.db')
cursor = connection.cursor()

#Выбор всех клиентов, которые преобрели телефизор со скидкой боьше чем 10%
cursor.execute('''SELECT
    C.id_orders,
    Cust.fio,
    C.order_date,
    C.location,
    C.skidka AS order_discount,  
    T.model_name,
    T.discount AS tv_discount, 
    OT.kolicestvo,
    OT.price_unit,
    OT.skidka AS order_tv_discount
FROM
    Client AS C
JOIN
    Customers AS Cust ON C.id_client = Cust.id_client
JOIN
    Order_tv AS OT ON C.id_orders = OT.id_orders
JOIN
    Tv AS T ON OT.id_tv = T.id_tv
WHERE
    T.discount > 0.10 
    AND C.order_date BETWEEN '2024-02-25' AND '2024-10-09';
    ''')

users = cursor.fetchall()
print(users)

print('/' * 50, '\n')
cursor.execute('''SELECT
    C.id_orders,
    Cust.fio,
    C.order_date,
    C.location
FROM
    Client AS C
JOIN
    Customers AS Cust ON C.id_client = Cust.id_client
WHERE
    Cust.fio LIKE 'А%' OR Cust.fio LIKE 'P%';
    ''')

users1 = cursor.fetchall()
print(users1)
print('\n')
print('Каков код производителя телевизора?')
cursor.execute('''SELECT
    id_proisvod
FROM
    Tv
''')
TV = cursor.fetchall()
print(TV)

print('\n')
print('Каково название модели телевизора?')
cursor.execute('''SELECT
    model_name
FROM
    Tv
''')
TV2 = cursor.fetchall()
print(TV2)
print('\n')

print('Каков размер диагонали телевизора  в дюймах ')
cursor.execute('''SELECT
    diagonal_size
FROM
    Tv
''')

TV3 = cursor.fetchall()
print(TV3)
print('\n')

print('Какова цена телевизора?')
cursor.execute('''SELECT
    price
FROM
    Tv
''')

TV4 = cursor.fetchall()
print(TV4)
print('\n')

print('Каков идентификатор клиента и Каковы ФИО клиента?')
cursor.execute('''SELECT
    id_client,
    fio
FROM
    Customers
''')

Cli = cursor.fetchall()
print(Cli)
connection.commit()
connection.close()
