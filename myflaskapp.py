from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
<<<<<<< HEAD
    return "Flask is updated"
=======
    return "Flask application properly functioning"
>>>>>>> 463b2eee6ee961f7e88f1101cb0cbba04a837f87

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)
