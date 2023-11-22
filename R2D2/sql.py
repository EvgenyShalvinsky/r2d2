import sqlite3
import config
import util


def connect():
    try:
        global base
        base = sqlite3.connect(config.BASE_PATH)
        util.write_log("Найден файл ДБ session.dll ")
        return base
    except:
        util.time("Не найден файл ДБ session.dll ")



def create_tables(base):
    try:
        con = base.cursor()
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
        util.write_bug("Ошибка создания таблицы users")

def add_user(base, id, name, username, role, date):
    try:
        base.cursor().execute(
            '''INSERT INTO adm(TgId, Name, UserName, Role, RegDate) VALUES (?,?,?,?,?)''',
            (id, name, username, role, date)
        )
        base.commit()
        util.write_log("Добавлена запись о сессии")
    except:
        util.write_bug("Ошибка добавления записи о сессии")

