import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

db_file = "tv_store.db"  # Глобальная переменная для имени файла БД
connection = None  # Глобальная переменная для соединения
cursor = None  # Глобальная переменная для курсора

def connect_to_db():
    """Подключается к базе данных и возвращает курсор."""
    global connection, cursor
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        create_tables(cursor)
        return cursor
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Не удалось подключиться к базе данных: {e}")
        exit()

def create_tables(cursor):
    """Создает таблицы в базе данных."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Proisvod(
        id_proisvod INTEGER PRIMARY KEY,
        name_proisvod VARCHAR NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers(
        id_client INTEGER PRIMARY KEY,
        fio VARCHAR NOT NULL
    )
    ''')

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


def get_table_names(cursor):
    """Возвращает список имен таблиц из базы данных."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def display_table_data(tree, selected_table):
    """Отображает данные выбранной таблицы в Treeview."""
    if not selected_table:
        return

    try:
        # Очищаем Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Получаем структуру таблицы
        cursor.execute(f"PRAGMA table_info({selected_table});")
        columns = [(col[1], col[2]) for col in cursor.fetchall()]  # имя и тип
        column_names = [col[0] for col in columns]

        # Настраиваем Treeview
        tree["columns"] = column_names
        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Получаем данные из таблицы
        cursor.execute(f"SELECT * FROM {selected_table}")
        data = cursor.fetchall()

        # Заполняем Treeview
        for row in data:
            tree.insert("", END, values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка при отображении данных: {e}")

def add_record(selected_table):
    """Открывает диалоговое окно для добавления записи."""
    if not selected_table:
        messagebox.showinfo("Информация", "Выберите таблицу.")
        return

    # Получаем структуру таблицы
    cursor.execute(f"PRAGMA table_info({selected_table});")
    columns = [(col[1], col[2]) for col in cursor.fetchall()]
    column_names = [col[0] for col in columns]

    AddEditDialog(root, "Добавить запись", selected_table, column_names, cursor, connection, lambda: display_table_data(tree, selected_table))

def delete_record(tree, selected_table):
    """Удаляет выбранную запись из таблицы."""
    if not selected_table:
        messagebox.showinfo("Информация", "Выберите таблицу.")
        return

    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("Информация", "Выберите запись для удаления.")
            return

        item_values = tree.item(selected_item[0], "values")

        # Определение имени столбца первичного ключа
        cursor.execute(f"PRAGMA table_info({selected_table});")
        columns_info = cursor.fetchall()
        primary_key_column = next((col[1] for col in columns_info if col[5] == 1), None)  # col[5]==1 означает первичный ключ

        if not primary_key_column:
            messagebox.showerror("Ошибка", "Не удалось определить первичный ключ таблицы.")
            return

        # Получение значения первичного ключа из выделенной записи
        primary_key_value_index = tree["columns"].index(primary_key_column)
        primary_key_value = item_values[primary_key_value_index]

        # Подтверждение удаления
        if messagebox.askyesno("Подтверждение", f"Вы уверены, что хотите удалить запись с {primary_key_column}={primary_key_value} из таблицы {selected_table}?"):
            sql = f"DELETE FROM {selected_table} WHERE {primary_key_column} = ?"
            cursor.execute(sql, (primary_key_value,))
            connection.commit()
            display_table_data(tree, selected_table)  # Обновление Treeview
            messagebox.showinfo("Успех", "Запись удалена.")

    except sqlite3.Error as e:
        connection.rollback()
        messagebox.showerror("Ошибка", f"Ошибка при удалении записи: {e}")


def update_record(tree, selected_table, root):
    """Изменяет существующую запись в таблице."""
    if not selected_table:
        messagebox.showinfo("Информация", "Выберите таблицу.")
        return

    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("Информация", "Выберите запись для редактирования.")
            return

        existing_values = tree.item(selected_item[0], "values")

        # Получаем структуру таблицы
        cursor.execute(f"PRAGMA table_info({selected_table});")
        columns = [(col[1], col[2]) for col in cursor.fetchall()]
        column_names = [col[0] for col in columns]

        AddEditDialog(root, "Редактировать запись", selected_table, column_names, cursor, connection, lambda: display_table_data(tree, selected_table), existing_values)

    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка при изменении записи: {e}")



class AddEditDialog: # Диалог для добавления и изменения
    def __init__(self, parent, title, table_name, column_names, cursor, connection, refresh_callback, existing_values=None):
        top = Toplevel(parent)
        top.title(title)

        entries = {}

        def add_new_record():
            """Добавляет новую запись в базу данных."""
            try:
                values = []
                for column in column_names:
                    values.append(entries[column].get())

                placeholders = ", ".join(["?"] * len(column_names))
                columns_str = ", ".join(column_names)

                sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
                cursor.execute(sql, tuple(values))
                connection.commit()
                messagebox.showinfo("Успех", "Запись добавлена.")
                refresh_callback() # Обновление
                top.destroy()

            except sqlite3.Error as e:
                connection.rollback()
                messagebox.showerror("Ошибка", f"Ошибка при добавлении записи: {e}")

        def save_changes():
            """Сохраняет изменения существующей записи."""
            try:
                # Определение имени столбца первичного ключа
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns_info = cursor.fetchall()
                primary_key_column = next((col[1] for col in columns_info if col[5] == 1), None) #col[5]==1 означает первичный ключ

                if not primary_key_column:
                    messagebox.showerror("Ошибка", "Не удалось определить первичный ключ таблицы.")
                    return

                # Получение значения первичного ключа из редактируемой записи
                primary_key_value = existing_values[column_names.index(primary_key_column)] # Берем значение первичного ключа

                set_clauses = []
                values = []

                for column in column_names:
                    set_clauses.append(f"{column} = ?")
                    values.append(entries[column].get()) # Все значения теперь нужно передавать в values

                sql = f"UPDATE {table_name} SET {', '.join(set_clauses)} WHERE {primary_key_column} = ?"

                # Добавляем значение primary key в values
                values.append(primary_key_value)

                cursor.execute(sql, tuple(values))

                connection.commit()
                messagebox.showinfo("Успех", "Запись изменена.")
                refresh_callback()
                top.destroy()

            except sqlite3.Error as e:
                connection.rollback()
                messagebox.showerror("Ошибка", f"Ошибка при сохранении изменений: {e}")

        # Создание виджетов диалогового окна
        for i, column in enumerate(column_names):
            label = Label(top, text=f"{column}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=W)

            entry_var = StringVar()
            if existing_values:
                entry_var.set(existing_values[i])
            entry = Entry(top, textvariable=entry_var)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=E)
            entries[column] = entry_var

         # Кнопки
        if existing_values:
            # Режим редактирования
            button = ttk.Button(top, text="Сохранить изменения", command=save_changes)
        else:
            # Режим добавления
            button = ttk.Button(top, text="Добавить", command=add_new_record)

        button.grid(row=len(column_names), column=0, columnspan=2, pady=10)


def main():
    """Создает главное окно и запускает приложение."""
    global root, tree, table_combobox # Делаем глобальными для доступа из функций
    cursor = connect_to_db() # Подключаемся к БД

    root = Tk()
    root.title("Управление базой данных")

    table_names = get_table_names(cursor) # Получаем список таблиц

    # Выбор таблицы
    table_label = Label(root, text="Выберите таблицу:")
    table_label.pack(pady=5)
    table_combobox = ttk.Combobox(root, values=table_names, state="readonly")
    table_combobox.pack(pady=5)
    table_combobox.bind("<<ComboboxSelected>>", lambda event: display_table_data(tree, table_combobox.get()))

    # Treeview для отображения данных
    tree = ttk.Treeview(root, show="headings")
    tree.pack(pady=5, fill=BOTH, expand=True)

    # Кнопки управления
    add_button = ttk.Button(root, text="Добавить запись", command=lambda: add_record(table_combobox.get()))
    add_button.pack(side=LEFT, padx=5, pady=5)
    delete_button = ttk.Button(root, text="Удалить запись", command=lambda: delete_record(tree, table_combobox.get()))
    delete_button.pack(side=LEFT, padx=5, pady=5)
    update_button = ttk.Button(root, text="Изменить запись", command=lambda: update_record(tree, table_combobox.get(), root))
    update_button.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
