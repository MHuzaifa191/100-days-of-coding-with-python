from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, func
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime
import os
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.subtitle = request.form['subtitle']
        post.author = request.form['author']
        post.body = request.form['content']
        post.date = datetime.now()

        db.session.commit()

        return redirect(url_for('show_post', post_id=post.id))

    return render_template('edit_post.html', post=post)


@app.route("/new-post", methods=["POST", "GET"])
def make_new_post():
    if request.method == "POST":
        title = request.form['title']
        subtitle = request.form.get('subtitle')
        author = request.form['author']
        date = request.form['date']
        content = request.form['content']
        image = request.form['image']
        highest_id = int(db.session.query(func.max(BlogPost.id)).scalar()) + 1

        new_post = BlogPost(
            id = highest_id,
            title=title,
            subtitle=subtitle,
            author=author,
            date=datetime.strptime(date, '%Y-%m-%d'),
            body=content,
            img_url=image
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    
    return render_template("make-post.html")


@app.route("/delete-post/<int:post_id>", methods=["POST", "GET"])
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully.", "success")
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/form-entry', methods=["POST", "GET"])
def collect_data():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        my_email = 'm.huz4if4@gmail.com'
        my_password = os.environ['gmail_pass']

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            subject = "Message from user"
            body = f"Message: {message}, from {name}"
            msg = f"Subject: {subject}\n\n{body}"
            connection.sendmail(from_addr=my_email, to_addrs="m.huz4if4@gmail.com", msg=msg)
            connection.close()


        return f"{name}, your message has been submitted successfully!"
    


if __name__ == "__main__":
    app.run(debug=True, port=5003)
