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

def insert(title,author,year,isbn):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    connect.commit()
    connect.close()

def view():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM bookstore")
    books = cursor.fetchall()
    connect.close()
    return books

def search(title="", author="", year="", isbn=""):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM bookstore WHERE title=?"
                   "OR author=?"
                   "OR year=?"
                   "OR isbn=?", (title,author,year,isbn))
    books = cursor.fetchall()
    connect.close()
    return books

def delete(id):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM bookstore WHERE id=?", (id,))
    connect.commit()
    connect.close()

def update(id,title,author,year,isbn):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=?"
                   "WHERE id=?", (title, author, year, isbn, id))
    connect.commit()
    connect.close()

def close():
    return True



connect()
# insert("Holy Bible", "Joseph Smith", 1823, 123456)
# print(view())

