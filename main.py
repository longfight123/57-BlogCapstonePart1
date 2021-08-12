"""Personal Blog (Capstone Part 1)

This 'Flask' app website is the first part of a 'Blog Capstone' project.
It has 2 pages: The index page and an individual blog post page.
The blog posts data are obtained from an API. 'Jinja' templating is used
to render 'Python' code inside the HTML templates.

This script requires that 'requests' and 'Flask' be installed within the Python
environment the user is running this script in.

"""

from flask import Flask, render_template
import requests

BLOGS_ENDPOINT = 'https://api.npoint.io/4af156202f984d3464c3'

app = Flask(__name__)

@app.route('/')
def home():
    """called when the user makes a GET request to the index URL
    """

    response = requests.get(BLOGS_ENDPOINT)
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    """a webpage for each individual blog post

    GET: individual blog post page
    """
    response = requests.get(BLOGS_ENDPOINT)
    response.raise_for_status()
    posts = response.json()
    return render_template('post.html', posts=posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)
