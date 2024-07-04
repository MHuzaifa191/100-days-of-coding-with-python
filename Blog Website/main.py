from flask import Flask, render_template
import requests


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


if __name__ == "__main__":
    app.run(debug=True)