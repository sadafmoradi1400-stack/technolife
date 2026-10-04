import sqlite3

DB_NAME = "MobileDetails.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS Mobiledata
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
storage TEXT,
ram TEXT,
color TEXT,
rating TEXT,
image TEXT,
link TEXT
)
'''
cursor.execute(query)

conn.commit()
conn.close()

print("DATABASE CREATED")


def save_product(title, description, storage, ram, color, rating, image, link):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = '''
    INSERT INTO Mobiledata
    (title, description, storage, ram, color, rating, image, link)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    cursor.execute(query,(title, description, storage, ram, color, rating, image, link))

    conn.commit()
    conn.close()