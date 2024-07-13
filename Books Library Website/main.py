from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

identity = 0

@app.route('/')
def home():
    db = sqlite3.connect("books-collection.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM books")
    books = res.fetchall()
    print(books)
    return render_template("index.html", books=books)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route('/add-book', methods=["POST", "GET"])
def collect_data():
    if request.method == 'POST':
        global identity
        name = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')
        identity += 1
        print(identity)
        db = sqlite3.connect("books-collection.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO books (id, title, author, rating) VALUES (?, ?, ?, ?)", (identity, name, author, rating))
        db.commit()
        cursor.close()

    db = sqlite3.connect("books-collection.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM books")
    books = res.fetchall()
    print(books)
    return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)

