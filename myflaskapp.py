from flask import Flask
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def display():
    return "Flask application properly functioning"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)



