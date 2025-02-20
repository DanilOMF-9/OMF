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
connection.commit()
connection.close()
