import sqlite3conn = Nonedef create_table():    cursor = conn.cursor()    query = """ CREATE TABLE IF NOT EXISTS cat(num INTEGER, name TEXT,date_of_birth TEXT,father TEXT,mother TEXT,gender INTEGER,photo BLOB,reserv INTEGER) """    cursor.execute(query)    conn.commit()    return "таблица создана"def init():    global conn    conn = sqlite3.connect('db/database.db')def get_cats():    init()    cursor = conn.cursor()    query = """ SELECT * FROM CAT     WHERE reserv = 0 """    cursor.execute(query)    conn.commit()    return cursor.fetchall()def db_sql(sql):    cursor = conn.cursor()    cursor.execute(sql)    conn.commit()    return cursordef quit():    conn.close()