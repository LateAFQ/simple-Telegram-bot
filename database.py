import sqlite3

conn = None


# создание таблицы если таковой нету
def create_table():
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS cat(num INTEGER, name TEXT,date_of_birth TEXT,father TEXT,mother TEXT,gender INTEGER,photo BLOB,reserv INTEGER) """
    cursor.execute(query)
    conn.commit()
    return "таблица создана"


# подключение к базе
def init():
    global conn
    conn = sqlite3.connect('db/database.db')


# вывод информации о кошках
def get_cats():
    response = db_sql("""
                    SELECT * 
                    FROM CAT 
                    WHERE reserv = 0
                    """).fetchall()

    return response


# выполнение sql запроса
def db_sql(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return cursor


def get_catboy():
    response = db_sql("""
                    SELECT *
                    FROM CAT 
                    WHERE reserv = 0 and gender = 1
                    """).fetchall()
    res_response = []
    for cat_info in response:
        res_response.append({
            'num': cat_info[0],
            'name': cat_info[1],
            'date_of_birth': cat_info[2],
            'father': cat_info[3],
            'mother': cat_info[4],
            'gender': cat_info[5],
            'photo': cat_info[6],
            'reserv': cat_info[-1]
        })
    return res_response


def get_catgirl():
    # init()
    response = db_sql("""
                    SELECT * 
                    FROM CAT 
                    WHERE reserv = 0 and gender = 0
                    """).fetchall()

    res_response = []
    for cat_info in response:
        res_response.append({
            'num': cat_info[0],
            'name': cat_info[1],
            'date_of_birth': cat_info[2],
            'father': cat_info[3],
            'mother': cat_info[4],
            'gender': cat_info[5],
            'photo': cat_info[6],
            'reserv': cat_info[-1]
        })
    return res_response

def get_boy_eng():
    response = db_sql("""
                    SELECT *
                    FROM CAT 
                    WHERE reserv = 0 and gender = 1
                    """).fetchall()
    res_response = []
    for cat_info in response:
        res_response.append({
            'num': cat_info[0],
            'name': cat_info[1] + " eng",
            'date_of_birth': cat_info[2],
            'father': cat_info[3],
            'mother': cat_info[4],
            'gender': cat_info[5],
            'photo': cat_info[6],
            'reserv': cat_info[-1]
        })
    return res_response

def get_girl_en():
    # init()
    response = db_sql("""
                    SELECT * 
                    FROM CAT 
                    WHERE reserv = 0 and gender = 0
                    """).fetchall()

    res_response = []
    for cat_info in response:
        res_response.append({
            'num': cat_info[0],
            'name': cat_info[1] + " eng",
            'date_of_birth': cat_info[2],
            'father': cat_info[3],
            'mother': cat_info[4],
            'gender': cat_info[5],
            'photo': cat_info[6],
            'reserv': cat_info[-1]
        })
    return res_response


# выход из базы
def quit():
    conn.close()


