from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    result = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = result.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def get_post(num):
    result = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = result.json()
    for post in all_posts:
        if int(post['id']) == int(num):
            return render_template("post.html", post=post)
    return "Not Found"

if __name__ == "__main__":
    app.run(debug=True)
