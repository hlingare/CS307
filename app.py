# ./app.py
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS
from database_connector import course_list, training_data, training, predicts, create_uid, predict_data
from machine_learning_service import ml_train, ml_distances, normalize
from machine_learning_no_data import ml_train_no, ml_predict_no
from sklearn.neighbors import NearestNeighbors
import psycopg2
from flask import request
import json
from json import JSONEncoder
from json import JSONDecoder
from operator import itemgetter


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yipgikbasudyog:21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2@ec2-54-163-229-169.compute-1.amazonaws.com:5432/df5g8vla4snv52'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


upvote = 0




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

@app.route('/result_list', methods=['POST'])
def result_list(text):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        uid = text
        currentUid = (uid,)
        uid = str(uid)
        courseList, options = course_list(uid)
        if (len(courseList) == 0):
            list_course = list_courses()
            ids = []
            for i in range(0, len(list_course)):
                ids.append(i)
            ml_train_no(ids)
            names, preds = ml_predict_no(ids, list_course)
            no_data_db(text, names, preds)
            return
        #print("courseList: ", courseList)
        #print("options: ", options)
        data_train = training_data(courseList)
        pred = predict_data(data_train)
        #print("data_train: ", data_train)
        norm_data = normalize(data_train,options)
        #print("normalized data: ", norm_data)
        n_neighbors = len(norm_data)
        #print("n_neighbors: ", n_neighbors)
        clf = NearestNeighbors(n_neighbors,  algorithm = 'kd_tree')
        training(norm_data, clf)
        distances = predicts(pred, clf)
        create_uid(uid, distances)
        return distances
    finally:
        if con:
            con.close()

@app.route('/get_result_list',methods=['GET'])
def get_result_list():
    con = None
    try:

        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.args.get('userId')
        result_list(text)

        currentUid = (text,)
        cur.execute('SELECT * FROM "{}"'.format(str(text)))
        rows = cur.fetchall()

        result = []
        for row in rows:
            grade = row[3]
            predGrade = "B"
            if grade >= 90:
                predGrade = "A"
            if grade >= 80 and grade < 90:
                predGrade = "B"
            if grade >= 70 and grade < 80:
                #print("A")
                predGrade = "C"
            if grade >= 60 and grade < 70:
                    #print("A")
                predGrade = "D"
            if grade < 60 :
                #print("A")
                predGrade = "F"
            getGlobalVote(row[1])
            obj = {
               'id': row[0],
               'name': row[1],
               'score': row[2],
               'upvote': upvote,
               'grade': predGrade
            }
            result.append(obj)

            response = jsonify(result)
             #response.status_code = 200
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
        currentCourse = (course_name,)
        cur.execute("SELECT * FROM student WHERE %s = uid",currentUID)
        rows = cur.fetchall()
        con.commit()
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

        #print("options: ", D)
        E = []
        #print("ROWS ", rows)
        cur.execute("SELECT options FROM course WHERE %s = name",currentCourse)
        cols = cur.fetchone()[0]
        con.commit()

        cur.execute("UPDATE student SET taken_course = %s WHERE %s = uid",(C,str(uid), ))
        cur.execute("UPDATE student SET option = %s WHERE %s = uid",(D,str(uid), ))
        con.commit()

        #print("COLS ",cols)
        #print("cols len: ", len(cols))
        E = cols
        #print("E: ",E)

        E.append((D[len(D) - 1]))
        #print("E AFTER APPEND: ",E)

        cur.execute("UPDATE course SET options = %s WHERE %s = name",(E,course_name,))

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
    #print("GETCOURSE")
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        #cur1 = con.cursor()
        courseName =  request.args.get('coursename')
        currentCourseName = (courseName,)
        cur.execute("SELECT idcourse,name,description,professor,timings,options,grade FROM course WHERE %s = name", currentCourseName)
        rows = cur.fetchall()
        result = []
        optionsArr = []
        for col in rows:
            #print("COL: ", col[5])
            optionsArr = col[5]
        sum = 0
        for i in range(0,len(optionsArr)):
            sum += float(optionsArr[i])
        if len(optionsArr) > 0:
            sum = sum / len(optionsArr)

        sum = round(sum,3)

        #print("SUM: ",sum)
        avgGrade = "B"
        if sum >= 11 and sum <= 11.667:
            avgGrade = "C"
        if sum > 11.667 and sum <= 12.334:
            avgGrade = "B"
        if sum > 12.334:
            #print("A")
            avgGrade = "A"
        #print("AVERAGE GRADE: ", avgGrade)

        cur.execute("UPDATE course SET grade = %s WHERE %s = name", (avgGrade, currentCourseName, ))
        #con.commit()
        cur.execute("SELECT idcourse,name,description,professor,timings,options,grade FROM course WHERE %s = name", currentCourseName)
        con.commit()

        for row in rows:
             #print(row,"row")
             obj = {
               'name': row[1],
               'description': row[2],
               'professor': row[3],
               'timings': row[4],
               'grade': row[6]
             }
             con.commit()
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
        #print(text)
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
             #print(row,"row")
             obj = {
               'upvote': row[0],
             }
             result.append(obj)
             #print (obj)
             response = jsonify(result = obj)
             response.status_code = 200
             return response

    finally:
        if con:
            con.close()
def getGlobalVote(name):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        courseName = name
        currentCourseName = (courseName,)
        cur.execute("SELECT upvote FROM course WHERE %s = name", currentCourseName)
        result = []
        for row in cur:
             obj = {
               'upvote': row[0],
             }
             global upvote
             upvote = obj["upvote"]
             result.append(obj)

             response = jsonify(result = obj)
             response.status_code = 200
             return response

    finally:
        if con:
            con.close()

@app.route('/getProfileURL', methods = ['GET'])
def getProfileURL():
     con = None
     try:
         con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
         cur = con.cursor()
         uid = request.args.get('uid')
         currentUID = (uid,)
         cur.execute("SELECT profile_pic FROM student WHERE %s = uid", currentUID)
         result = []
         for row in cur:
              obj = {
                'username': row[0],
              }
              result.append(obj)
              response = jsonify(result)
              response.status_code = 200
              return response
     finally:
         if con:
             con.close()

@app.route('/postProfileURL')
def postProfileURL():
    con = None
    taken_course = []
    option = []
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        text = request.data
        dart = json.loads(text)
        uid = dart["userID"]
        currentUid = (uid,)
        profileId = dart["profileID"]
        cur.execute("UPDATE student SET profile_pic = %s WHERE uid = %s", (profileId, currentUid,))
        con.commit()
        response.status_code = 200
        return response
    finally:
        if con:
            con.close()


if __name__ == '__main__':
          port = 5000 #the custom port you want
          app.run(debug=True)
          #app.run(host='0.0.0.0', port=port)
