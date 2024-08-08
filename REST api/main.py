from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import sqlite3
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route('/random')
def get_cafe():
    db = sqlite3.connect("instance/cafes.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM cafe")
    cafes = res.fetchall()
    db.close()
    selected_cafe = random.choice(cafes)
    cafe_data = {
        "id": selected_cafe[0],
        "name": selected_cafe[1],
        "location_url": selected_cafe[2],
        "image_url": selected_cafe[3],
        "location": selected_cafe[4],
        "seats_available": selected_cafe[5],
        "has_toilet": selected_cafe[6],
        "has_wifi": selected_cafe[7],
        "has_sockets": selected_cafe[8],
        "coffee_price": selected_cafe[9],
        "price": selected_cafe[10],
    }

    return jsonify(cafe_data)


@app.route('/all')
def get_all_cafes():
    db = sqlite3.connect("instance/cafes.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM cafe")
    cafes = res.fetchall()
    db.close()
    all_cafes = []
    for selected_cafe in cafes:
        cafe_data = {
            "id": selected_cafe[0],
            "name": selected_cafe[1],
            "location_url": selected_cafe[2],
            "image_url": selected_cafe[3],
            "location": selected_cafe[4],
            "seats_available": selected_cafe[5],
            "has_toilet": selected_cafe[6],
            "has_wifi": selected_cafe[7],
            "has_sockets": selected_cafe[8],
            "coffee_price": selected_cafe[9],
            "price": selected_cafe[10],
        }
        all_cafes.append(cafe_data)

    return jsonify(all_cafes)

@app.route('/search')
def search_cafe():
    location = request.args.get('location')
    db = sqlite3.connect("instance/cafes.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT * FROM cafe")
    cafes = res.fetchall()
    db.close()
    for selected_cafe in cafes:
        if selected_cafe[4] == location:
            cafe_data = {
            "id": selected_cafe[0],
            "name": selected_cafe[1],
            "location_url": selected_cafe[2],
            "image_url": selected_cafe[3],
            "location": selected_cafe[4],
            "seats_available": selected_cafe[5],
            "has_toilet": selected_cafe[6],
            "has_wifi": selected_cafe[7],
            "has_sockets": selected_cafe[8],
            "coffee_price": selected_cafe[9],
            "price": selected_cafe[10],
        }
            return jsonify(cafe_data)
    return jsonify({"error": "No cafes found in this location"})

# HTTP POST - Create Record


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    if request.method == 'POST':
        db = sqlite3.connect("instance/cafes.db")
        cursor = db.cursor()
        res = cursor.execute("SELECT * FROM cafe")
        cafes = res.fetchall()
        id = cafes[-1][0] + 1
        name = request.form.get('name')
        map_url = request.form.get('map_url')
        image_url = request.form.get('image_url')
        location = request.form.get('location')
        seats_available = request.form.get('seats_available')
        has_toilet = request.form.get('has_toilet')
        has_wifi = request.form.get('has_wifi')
        has_sockets = request.form.get('has_sockets')
        coffee_price = request.form.get('coffee_price')
        can_take_calls = request.form.get('can_take_calls')
        cursor.execute("INSERT INTO cafe (id, name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, name, map_url, image_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats_available, coffee_price))
        db.commit()
        cursor.close()
        db.close()
        response = {
            "success" : "Successfully added the new cafe."
        }
        return jsonify(response)
    else:
        response = {
            "failed" : "Wrong method."
        }
        return jsonify(response)




# HTTP PUT/PATCH - Update Record

@app.route('/update/<int:cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    try:
        new_price = request.form.get('new_price')
        if not new_price:
            return jsonify({"error": "New price not provided"}), 400
        db = sqlite3.connect("instance/cafes.db")
        cursor = db.cursor()
        cursor.execute("UPDATE cafe SET coffee_price = ? WHERE id == ?", (new_price, cafe_id))
        db.commit()
        response = {
            "success" : "Successfully updated price"
        }
        cursor.close()
        db.close()
        return jsonify(response)
    except Exception as e:
        print('Exception: {}'.format(e))
        # raise Exception(e)
        response = {
                "Exception" : '{}'.format(e)
        }
        return jsonify(response)
        


# HTTP DELETE - Delete Record

@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def close_cafe(cafe_id):
    api_key = request.form.get('api-key')
    if api_key != 'TopSecretAPIKey':
        return jsonify({"error": "Make sure correct api key is provided"}), 400
    else:
        try:
            db = sqlite3.connect("instance/cafes.db")
            cursor = db.cursor()
            cursor.execute("DELETE FROM cafe WHERE id == ?", (cafe_id,))
            db.commit()
            response = {
                "success" : "Successfully deleted cafeteria from database"
            }
            cursor.close()
            db.close()
            return jsonify(response)
        except Exception as e:
            print('Exception: {}'.format(e))
            response = {
                    "Exception" : '{}'.format(e)
            }
            return jsonify(response), 400




if __name__ == '__main__':
    app.run(debug=True)
