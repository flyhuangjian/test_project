# !/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>')
def get_name(username):
    return username

@app.route('/')
def index():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True, port=8787)