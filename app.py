# ./app.py
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS
from database_connector import read
from machine_learning_service import ml_train, ml_predict, normalize
from sklearn import neighbors
import psycopg2
from flask import request
import json
from json import JSONEncoder
from json import JSONDecoder

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yipgikbasudyog:21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2@ec2-54-163-229-169.compute-1.amazonaws.com:5432/df5g8vla4snv52'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World1!"

@app.route('/prereg')
def prereg():
      sql = text("SELECT * FROM Course")
      result = db.engine.execute(sql)
      results = []
      for row in result:
          obj = {
            'id': row.idcourse,
            'title': row.name,
          }
          results.append(obj)

      response = jsonify(results)
      response.status_code = 200
      return response

@app.route('/result_list')
def result_list():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        cur.execute("SELECT * FROM courseList")
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        temp = []
        for row in rows:
            temp.append(list(row))

        courses = []
        for i in range(0, len(temp)):
            courses.append(temp[i][1])

        n_neighbors = 4
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
        train_data = read(0)
        pred_data = read(1)
        ml_train(train_data, clf)
        predicts = ml_predict(pred_data, clf)
        fin_pred = []
        for i in range(0, len(predicts)):
            if (predicts[i] == 0):
                string = "Yes: " + courses[i]
                fin_pred.append(string)
            else:
                string = "No: " + courses[i]
                fin_pred.append(string)

        response = jsonify(fin_pred)
        response.status_code = 200
        return response
    finally:
        if con:
            con.close()

@app.route('/showStudent', methods=['POST'])
def studentinfo():
    con = None
    taken_course = []
    option = []
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.data
        dart = json.loads(text)
        uid = dart["userId"]
        username = dart["name"]
        query = "INSERT INTO student (uid, username, taken_course, option) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (uid, username, taken_course, option))
        con.commit()
        response.status_code = 200
        return response
    finally:
        if con:
            con.close()
@app.route ('/showCourse', methods=['POST'])
def courseInfo():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.data
        dart = json.loads(text)
        uid = dart["userId"]
        options = dart["option"]
        currentUID = (uid,)
        course_name = dart["course_name"]
        cur.execute("SELECT * FROM student WHERE %s = uid",currentUID)
        rows = cur.fetchall()
        temp = []
        for row in rows:
             temp.append(list(row))
        reads = []
        for i in range(0, len(temp)):
             temps = []
             for j in range(0, len(temp[i])):
                 temps.append(temp[i][j])
             reads.append(temps)
        if(len(reads) == 0):
           return "ERROR"
        if course_name not in reads[0][2]:
            reads[0][2].append(course_name)
            reads[0][3].append(options)
        else:
            return "Course Exists!!"
        C = reads[0][2]
        D = reads[0][3]
        cur.execute("UPDATE student SET taken_course = %s WHERE %s = uid",(C,str(uid), ))
        cur.execute("UPDATE student SET option = %s WHERE %s = uid",(D,str(uid), ))

        con.commit()
        return reads
    finally:
        if con:
            con.close()
@app.route('/updateUsername', methods = ['POST'])
def updateUsername():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.data
        dart = json.loads(text)
        uid = dart["userId"]
        currentUID = (uid,)
        username = dart["name"]
        cur.execute("UPDATE student SET username = %s WHERE %s = uid",(username,currentUID, ) )
        con.commit()
        response.status_code = 200
        return response
    finally:
        if con:
            con.close()

@app.route('/getCourse', methods = ['GET'])
def getCourse():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        courseName =  request.args.get('coursename')
        currentCourseName = (courseName,)
        cur.execute("SELECT idcourse,name,description,professor,timings FROM course WHERE %s = name", currentCourseName)
        result = []
        for row in cur:
             print(row,"row")
             obj = {
               'name': row[1],
               'description': row[2],
               'professor': row[3],
               'timings': row[4],
             }
             result.append(obj)
             response = jsonify(result = obj)
             response.status_code = 200
             return response
    finally:
        if con:
            con.close()
@app.route('/getUserName', methods = ['GET'])
def getUserName():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        uid = request.args.get('uid')
        currentUID = (uid,)
        cur.execute("SELECT username FROM student WHERE %s = uid", currentUID)
        result = []
        for row in cur:
             print(row,"row")
             obj = {
               'username': row[0],
             }
             result.append(obj)
             response = jsonify(result = obj)
             response.status_code = 200
             return response
    finally:
        if con:
            con.close()

@app.route('/postVote', methods = ['POST'])
def postVote():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.data
        print(text)
        dart = json.loads(text)
        vote = dart["upvote"]
        currentVote = (vote,)
        coursename = dart["courseName"]
        cur.execute("UPDATE course SET upvote = %s WHERE %s = name",(currentVote,coursename,))
        con.commit()
        response.status_code = 200
        return response
    finally:
        if con:
            con.close()


@app.route('/getVote', methods = ['GET'])
def getVote():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        courseName = request.args.get('courseName')
        currentCourseName = (courseName,)
        cur.execute("SELECT upvote FROM course WHERE %s = name", currentCourseName)
        result = []
        for row in cur:
             print(row,"row")
             obj = {
               'upvote': row[0],
             }
             result.append(obj)
             print (obj)
             response = jsonify(result = obj)
             response.status_code = 200
             return response

    finally:
        if con:
            con.close()

if __name__ == '__main__':
          port = 5000 #the custom port you want
          app.run(debug=True)
          #app.run(host='0.0.0.0', port=port)
