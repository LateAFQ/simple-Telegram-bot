import sqlite3import base64conn = None#создание таблицы если таковой нетуdef create_table():    cursor = conn.cursor()    query = """ CREATE TABLE IF NOT EXISTS cat(num INTEGER, name TEXT,date_of_birth TEXT,father TEXT,mother TEXT,gender INTEGER,photo BLOB,reserv INTEGER) """    cursor.execute(query)    conn.commit()    return "таблица создана"#подключение к базеdef init():    global conn    conn = sqlite3.connect('db/database.db')#вывод информации о кошкахdef get_cats():    init()    response = db_sql(            """ SELECT * FROM CAT             WHERE reserv = 0 """).fetchall()    return print(response)#выполнение sql запросаdef db_sql(sql):    cursor = conn.cursor()    cursor.execute(sql)    conn.commit()    return cursor#выход из базыdef quit():    conn.close()def get_catboy():    init()    response = db_sql(            """ SELECT * FROM CAT             WHERE reserv = 0 and gender = 1""").fetchall()    return responsedef get_catgirl():    init()    response = db_sql(        """ SELECT * FROM CAT         WHERE reserv = 0 and gender = 0""").fetchall()    return response