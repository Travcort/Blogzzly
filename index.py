from flask import Flask, render_template
from markupsafe import escape
import requests, os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
notionProxy = os.getenv("NOTION_PROXY_URL")

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

def get_posts():
    response = requests.get(f'{notionProxy}/blogs')
    response.raise_for_status()
    return response.json()['data']

def get_single_post(slug):
    response = requests.get(f'{notionProxy}/blogs/{slug}')
    response.raise_for_status()
    return response.json()['data']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = get_posts()
    return render_template('Blog.html', Posts=posts)

@app.route('/blog/<string:slug>')
def post(slug):
    article = get_single_post(escape(slug))
    return render_template('Post.html', post=article)

@app.route('/contact')
def contact():
    return render_template('Contact.html')

if __name__ == '__main__' and os.getenv("APP_ENV") == "Development":
    app.run(debug=True)