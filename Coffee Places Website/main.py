from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    return render_template('add.html', form=form)


@app.route('/form-entry', methods=["POST", "GET"])
def collect_data():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        opening = request.form.get('open')
        closing = request.form.get('close')
        coffee = u'☕'* int(request.form.get('coffee', 0))
        wifi = u'💪' * int(request.form.get('wifi', 0))
        power = u'🔌' * int(request.form.get('power', 0))

        if (int(request.form.get('wifi', 0)) == 0):
            wifi = u'✘'

        fields = [name, location, opening, closing, coffee, wifi, power]
        print(fields)

        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fields)



    return render_template('add.html')


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
