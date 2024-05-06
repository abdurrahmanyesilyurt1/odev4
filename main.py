import sqlite3

# Veritabanı bağlantısını ve tabloyu elle kurma
conn = sqlite3.connect('metinler.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS metinler (id INTEGER PRIMARY KEY, content TEXT)')

def add_text_to_db(text, cursor):
    cursor.execute('INSERT INTO metinler (content) VALUES (?)', (text,))

text1 = "Bu bir örnek metindir ve bazı ortak kelimeler içerir."
text2 = "Bu metin de örnek bir metindir ve ortak kelimeler içermektedir."

add_text_to_db(text1, c)
add_text_to_db(text2, c)

conn.commit()
conn.close()