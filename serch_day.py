import sqlite3

def selectday(day):
    try:

        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM WeekDat WHERE  d = ?;"
        cursor.execute(sqlite_select_query, (day,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

def createTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS WeekDat (
                                    d TEXT PRIMARY KEY,
                                    day TEXT NOT NULL
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def insertManyData(records):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth7.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        insert_data_query = '''INSERT INTO WeekDat( d,day)
                               VALUES (?, ?);'''
        cursor.executemany(insert_data_query, records)
        sqlite_connection.commit()
        print("Записей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

records=[('Sat','суббота'),
         ('Sun','воскресенье'),
         ('Mon','понедельник'),
         ('Tue','вторник'),
         ('Wed','среда'),
         ('Thu','четверг'),
         ('Fri','пятница')]


