import sqlite3def create_table():    with sqlite3.connect('db/database.db') as db:        cursor = db.cursor()        query = """ CREATE TABLE IF NOT EXISTS cat(num INTEGER, name TEXT,date_of_birth TEXT,father TEXT,mother TEXT,gender INTEGER,photo BLOB) """        cursor.execute(query)        db.commit()