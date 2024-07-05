from flask import Flask, render_template, request
import requests
import os 
import smtplib


app = Flask(__name__)

@app.route('/templates/index.html')
@app.route('/')
def home():
    result = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
    all_posts = result.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def get_post(num):
    result = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
    all_posts = result.json()
    for p in all_posts:
        if int(p['id']) == int(num):
            return render_template("post.html", post=p)
    return "Not Found"

@app.route('/templates/about.html')
def about():
    return render_template("about.html")

@app.route('/templates/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/form-entry', methods=["POST", "GET"])
def collect_data():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        message = f"""Hi there\n

                Sender: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}"""

        send = f"Sender: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}"

        my_email = 'm.huz4if4@gmail.com'
        my_password = os.environ['gmail_pass']
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
        connection.close()

        return f"{name}, your message has been submitted successfully!"
    





if __name__ == "__main__":
    app.run(debug=True)