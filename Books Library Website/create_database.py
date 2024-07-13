import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INT IDENTITY(1,1) PRIMARY KEY NOT NULL, title varchar(250) NOT NULL, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
db.commit()

# cursor.execute("INSERT INTO books (id, title, author, rating) VALUES(2, 'name', 'author', 'rating')")
# db.commit()
# res = cursor.execute("SELECT * FROM books")
# print(res.fetchall())