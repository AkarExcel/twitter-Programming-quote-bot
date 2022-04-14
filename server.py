# server.py file
from os import environ
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return"Home page"

app.run(host= '0.0.0.0', port=environ.get('PORT'))



