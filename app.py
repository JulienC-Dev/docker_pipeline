import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello word, I am a live Flask application!'
'''ATTENTION : LEAK DATA dans le cadre du projet
user="root",
password="p@ssw0rd1"
'''