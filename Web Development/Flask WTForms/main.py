from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = MyForm()
    return render_template("login.html", form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        print(f"Name: {name}, Password: {password}")
        return render_template('success.html', form=form)
    return render_template('submit.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
