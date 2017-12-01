# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:11:27 2017
@author: Vishaal Bommena
"""
import psycopg2
from random import randint
from machine_learning_service import normalize, ml_train, ml_distances
from machine_learning_no_data import ml_train_no, ml_predict_no
from sklearn.neighbors import NearestNeighbors

def add_course(id_stud, course_name, options):
    con = None
    try:         
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        temps = (id_stud, )
        cur.execute("SELECT * FROM student WHERE %s = uid", temps)
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
        
        if (len(reads) == 0):
            return "ERROR"
        if course_name not in reads[0][2]:
            reads[0][2].append(course_name)
            reads[0][3].append(options)
        else: 
            return "Course Exists!!"
        
        C = reads[0][2]
        D = reads[0][3]
        
        print("D: ", D)
        E = []
        E.append( D[len(D) - 1])
        
        cur.execute("update student SET taken_course = %s WHERE uid = %s", (C, str(id_stud), ))
        cur.execute("update student SET option = %s WHERE uid = %s", (D, str(id_stud), ))
        cur.execute("update course SET options = %s WHERE name = %s", (E, str(course_name), ))
        con.commit()
        print("reads: ", reads)
        return reads
    finally:        
        if con:
            con.close()

def create(option):
    if (option == 0):
        try: 
            conn = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS student")
            cur.execute("CREATE TABLE student(UID Int PRIMARY KEY NOT NULL, username text, name text, taken_course text[], option text[])")
            conn.commit()
            cur.close()
<<<<<<< HEAD
            #print(rows_deleted)
            #print(cur.rowcount)
    finally:
        if (conn is not None):
            conn.close()
=======
        finally:
             if (conn is not None):
                conn.close()
        return "done"
    return "error"

>>>>>>> Changes in Machine Learning added No Data Machine Learning

def training(train_data, clf):
    ml_train(train_data, clf)

def predicts(predict_data, clf):
    distances = ml_distances(predict_data, clf)
    return distances

def training_data(course_list):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        fin_traits = []
        for i in range(0, len(course_list)):
            traits = []
            course_name = course_list[i].lower()
            temps = (course_name,)
            #print("name: ", temps)
            cur.execute("SELECT trait FROM course WHERE %s = name", temps)
            rows = cur.fetchall()
            temp = []
            for row in rows:
                temp.append(list(row))
            traits = []
            #print("temp: ", temp)
            for j in range(0,len(temp[0][0])):
                traits.append(int(temp[0][0][j]))
            fin_traits.append(traits)
            con.commit()
        return fin_traits
    finally:
         if con:
             con.close()

def course_list(id_stud):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        temps = (id_stud, )
        #print("IDSTUD: ", id_stud)
        cur.execute("SELECT taken_course FROM student WHERE %s = uid", temps)
        rows = cur.fetchall()
        temp = []
        #print("ROWS: ", rows)
        #print("TEMPS: ", temps)
        for row in rows:
            temp.append(list(row))
        #print("TEMP: ", temp)
        courses = []
        for i in range(0,len(temp[0][0])):
            courses.append(temp[0][0][i])
        option = []
        cur.execute("SELECT option FROM student WHERE %s = uid", temps)
        rows = cur.fetchall()
        temp = []
        for row in rows:
            temp.append(list(row))
        for i in range(0,len(temp[0][0])):
            option.append(temp[0][0][i])
        con.commit()
        return courses,option
    finally:
         if con:
             con.close()

def list_courses():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        cur.execute("SELECT name FROM course")
        rows = cur.fetchall()
        temp = []
        for row in rows:
            temp.append(list(row))
        courses = temp
        return courses
    finally:
         if con:
             con.close()

def predict_data(train_traits):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        tempa = ()
        for i in range(0, len(train_traits)):
            tempa = tempa + (train_traits[i], )
        cur.execute("SELECT trait FROM course WHERE trait not in %s", (tempa, ))
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        temp = []
        for row in rows:
            temp.append(list(row))
        trait = []
        temp1 = []
        for i in range(0,len(temp)):
            for j in range(0,len(temp[0])):
                temp1.append(temp[i][j])
        temp4 = []
        for i in range(0,len(temp1)):
            temp3 = []
            for j in range(0, len(temp1[0])):
                temp3.append(int(temp1[i][j]))
            temp4.append(temp3)
        trait = temp4
        return (trait)
    finally:
         if con:
             con.close()

def create_uid(uid, course_list):
    print("Creating a new UID")
    try:
        conn = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = conn.cursor()
        names = []
        scores = []
        for i in range(0, len(course_list)):
            traits_list = []
            for j in range(0, len(course_list[i])):
                if (j < len(course_list[i]) - 1):
                    traits_list.append(course_list[i][j])
                else:
                    scores.append(course_list[i][j])
            cur2 = conn.cursor()
            cur2.execute("SELECT * FROM course WHERE trait = %s", (traits_list, ))
            rows = cur2.fetchall()
            names.append(rows[0][1])
            conn.commit()
            cur2.close()
        temps = (uid, )
        query = 'DROP TABLE IF EXISTS "{}"'.format(str(uid))
        print("dropped the table")
        cur.execute(query)
        conn.commit()
        fin_list = []
        for i in range(0, len(names)):
            temp = []
            temp.append(names[i])
            temp.append(scores[i])
            fin_list.append(temp)
        fin_list = sorted(fin_list,key=itemgetter(1))
        query = 'create table "{}"(ID INT NOT NULL PRIMARY KEY, name TEXT, score INT, predGrade INT)'.format(str(uid))
        cur.execute(query)
        conn.commit()
        for i in range(0, len(fin_list)):
            querry = ('INSERT INTO "{}"(ID, name, score, predGrade) VALUES (%s, %s, %s, %s)'.format(str(uid)))
            pGrade = ((17 - int(fin_list[i][1])) / 17) * 100
            cur.execute(querry, (i, fin_list[i][0], fin_list[i][1],pGrade))
        for i in range(0, len(fin_list)):
            print("changed list: ", fin_list[i][0])
        conn.commit()
        cur.close()
    finally:
         if (conn is not None):
            conn.close()

def no_data_db(uid, names, preds):
    try:
        conn = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = conn.cursor()
        temps = (uid, )
        query = 'DROP TABLE IF EXISTS "{}"'.format(str(uid))
        print("dropped the table")
        cur.execute(query)
        conn.commit()
        fin_list = []
        query = 'create table "{}"(ID INT NOT NULL PRIMARY KEY, name TEXT, score FLOAT, predGrade INT)'.format(str(uid))
        cur.execute(query)
        conn.commit()
        for i in range(0, len(names)):
<<<<<<< HEAD
            #print(names[i])
            querry = ('INSERT INTO "{}"(ID, name, score) VALUES (%s, %s, %s)'.format(str(uid)))
            cur.execute(querry, (i, names[i], scores[i]))
=======
            querry = ('INSERT INTO "{}"(ID, name, score, predGrade) VALUES (%s, %s, %s, %s)'.format(str(uid)))
            pGrade = 0
            cur.execute(querry, (i, names[i], 0, pGrade))
>>>>>>> Changes in Machine Learning added No Data Machine Learning
        conn.commit()
        cur.close()
    finally:
         if (conn is not None):
            conn.close()


def testing(text):
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
        print("courseList: ", courseList)
        print("options: ", options)
        data_train = training_data(courseList)
        pred = predict_data(data_train)
        print("data_train: ", data_train)
        norm_data = normalize(data_train,options)
        print("normalized data: ", norm_data)
        n_neighbors = len(norm_data)
        print("n_neighbors: ", n_neighbors)
        clf = NearestNeighbors(n_neighbors,  algorithm = 'kd_tree')
        training(norm_data, clf)
        distances = predicts(pred, clf)
        create_uid(uid, distances)
        return distances
    finally:
        if con:
            con.close() 