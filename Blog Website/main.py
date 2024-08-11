from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, Column
from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_login import login_required, current_user
import os
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('flask_key')
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.id == 1:
            return function(*args, **kwargs)
        else:
            return abort(403)
    return wrapper_function




# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
            


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)
    body = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('user_table.id'), nullable=False)
    img_url = Column(String(250), nullable=False)
    
    # Relationship to User
    author = relationship("User", back_populates="posts")

    # Relationship to Comment
    comments = relationship("Comment", back_populates="post")


class User(UserMixin, db.Model):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(1000), nullable=True)  

    # Relationship to BlogPost
    posts = relationship("BlogPost", back_populates="author")

    # Relationship to Comment
    comments = relationship("Comment", back_populates="user")


class Comment(db.Model): 
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey('blog_posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_table.id'), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)

    # Relationship to BlogPost
    post = relationship("BlogPost", back_populates="comments")

    # Relationship to User
    user = relationship("User", back_populates="comments")


with app.app_context():
    db.create_all()


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        print(f"Name: {name}, Password: {password}")

        hashed_password = generate_password_hash(password ,method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, name=name, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        # login_user(new_user)

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('get_all_posts'))
        elif user is None:
            flash('No account found with that email address.', 'danger')
        else:
            flash('Password is incorrect, please try again.')
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    try:
        result = db.session.execute(db.select(BlogPost))
        posts = result.scalars().all()
        print(f"Posts retrieved: {posts}") 
        return render_template("index.html", all_posts=posts)
    except Exception as e:
        print(f"Error: {e}") 
        return "An error occurred"
    


@app.route("/post/<int:post_id>", methods=["POST", "GET"])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if form.validate_on_submit() and current_user.is_authenticated:
        new_comment = Comment(
            text=form.comment_editor.data,
            user=current_user,
            post=requested_post,
            date=datetime.now()  # or func.now()
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template("post.html", post=requested_post, form=form)


@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=datetime.utcnow()  # Use datetime object here
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    
    if current_user.id == post_to_delete.author_id:
        comments_to_delete = Comment.query.filter_by(post_id=post_id).all()
        for comment in comments_to_delete:
            db.session.delete(comment)
        
        db.session.delete(post_to_delete)
        db.session.commit()
    else:
        flash("You don't have permission to delete this post.")
    
    return redirect(url_for('get_all_posts'))



@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/form-entry', methods=["POST", "GET"])
def collect_data():
    msg_sent = False
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
            msg_sent = True

        return render_template("contact.html", msg_sent=msg_sent)

    



if __name__ == "__main__":
    app.run(debug=True)
