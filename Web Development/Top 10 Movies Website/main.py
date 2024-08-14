from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    db = sqlite3.connect("movies-list.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM movies")
    movies = res.fetchall()
    print(movies)
    cursor.close()
    db.commit()
    db.close()
    return render_template("index.html", movies=movies)

@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/edit/<num>")
def edit(num):
    return render_template("edit.html", number=num)

@app.route("/change/<identity>", methods=["POST", "GET"])
def collect_data(identity):
    if request.method == 'POST':
        new_rating = request.form.get('rating')
        db = sqlite3.connect("movies-list.db")
        cursor = db.cursor()
        res = cursor.execute(f"UPDATE movies SET rating = {new_rating} WHERE id == {identity}")
        print(new_rating, identity)
        cursor.execute("UPDATE movies SET rating = ? WHERE id = ?", (new_rating, identity))
        cursor.close()
        db.commit()
        db.close()
    else:
        print("Method not post")
    return redirect(url_for('home'))

@app.route("/add-data", methods=["POST", "GET"])
def collect_movie_data():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        description = request.form.get('description')
        rating = request.form.get('rating')
        ranking = request.form.get('ranking')
        review = request.form.get('review')
        img_url = request.form.get('url')


        db = sqlite3.connect("movies-list.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO movies (id, title, year, description, rating, ranking, review, img_url) VALUES (? ,? ,? ,? ,? ,? ,? ,?)", (ranking, title, year, description, rating, ranking, review, img_url))
        cursor.close()
        db.commit()
        db.close()
    else:
        print("Method not post")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
