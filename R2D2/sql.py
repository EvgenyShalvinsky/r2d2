import sqlite3
import config
import util


def connect():
    try:
        global base
        base = sqlite3.connect(config.BASE_PATH)
        util.write_log("Найден файл ДБ shop.dll ")
        return base
    except:
        util.time("Не найден файл ДБ shop.dll ")



def create_tables(base):
    try:
        con = base.cursor()
        con.execute(
            '''CREATE TABLE IF NOT EXISTS goods
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        Code INTEGER,
                        Name TEXT,
                        Price INTEGER,
                        Description TEXT,
                        AddDate NUMERIC
                        )'''
                    )
        con.execute(
            '''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        TgId TEXT,
                        Name TEXT,
                        UserName TEXT,
                        Role TEXT,
                        RegDate NUMERIC
                        )'''
        )
        base.commit()
        util.write_log("Создана таблица users")
    except:
        util.write_bug("Ошибка создания Таблиц")

def add_user(base, id, name, username, role, date):
    try:
        base.cursor().execute(
            '''INSERT INTO adm(TgId, Name, UserName, Role, RegDate) VALUES (?,?,?,?,?)''',
            (id, name, username, role, date)
        )
        base.commit()
        util.write_log("Добавлен администратор")
    except:
        util.write_bug("Ошибка добавления администратора")

def update_goods(base, num, name, cost, descr, date):
    try:
        base.cursor().execute(
            '''INSERT INTO goods(Code, Name, Price, Description, AddData) VALUES (?,?,?,?,?)''',
            (num, name, cost, descr, date)
        )
        base.commit()
        util.write_log("Добавлен товар "+str(name))
    except:
        util.write_bug("Ошибка добавления товара "+str(name))

def update_catalog(base, num, price):
    try:
        base.cursor().execute(
            '''INSERT INTO catalog(GoodNumber, Price) VALUES (?,?)''',
            (num, price)
        )
        base.commit()
        util.write_log("Добавлен администратор")
    except:
        util.write_bug("Ошибка добавления администратора")