import sqlite3

def connect():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY,"
                   "title TEXT,"
                   "author TEXT,"
                   "year INTEGER,"
                   "isbn INTEGER)"
                   )
    connect.commit()
    connect.close()

def insert(item,author,year,isbn):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(item, author, year, isbn))
    connect.commit()
    connect.close()

def view():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM bookstore")
    books = cursor.fetchall()
    connect.close()
    return books

connect()
# insert("Holy Bible", "Joseph Smith", 1823, 123456)
print(view())

