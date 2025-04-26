import psycopg2
import pandas as pd

# Подключение к базе
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="634548mmm",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE,
            phone VARCHAR(20)
        )
    """)
    conn.commit()

def show_all():
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()
    if not rows:
        print("Телефонная книга пуста.")
    else:
        print("Список контактов:")
        for row in rows:
            print(f"{row[0]}. {row[1]} — {row[2]}")

# Добавление данных вручную
def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print(f"Контакт {name} добавлен")

# Загрузка из CSV
def insert_from_csv(csv):
    df = pd.read_csv(csv)
    for _, row in df.iterrows():
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row['username'], row['phone']))
    print(f"Контакты из файла добавлены")
    conn.commit()

# Обновление данных
def update_user():
    name = input("Имя пользователя, которого хочешь изменить: ")
    new_name = input("Новое имя (если не нужно менять — Enter): ")
    new_phone = input("Новый телефон (если не нужно менять — Enter): ")
    if new_name:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    conn.commit()
    print(f"Контакт {name} обновлен")

# Поиск
def search():
    value = input("Введите имя или телефон для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s OR phone = %s", (f"%{value}%", value))
    for row in cur.fetchall():
        print(row)

# Удаление
def delete():
    value = input("Введите имя или телефон для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (value, value))
    print(f"Контакт {value} удален")
    conn.commit()

# Меню
def menu():
    create_table()
    while True:
        print("\n1. Добавить вручную\n2. Загрузить из CSV\n3. Изменить данные\n4. Поиск\n5. Удалить\n6. Отобразить список\n7. Выйти")
        choice = input("Выбери действие: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv("C:\\Users\\user\\Desktop\\Python\\lab10\\csv.csv")
        elif choice == "3":
            update_user()
        elif choice == "4":
            search()
        elif choice == "5":
            delete()
        elif choice == "6":
            show_all()
        elif choice == "7":
            break
menu()
