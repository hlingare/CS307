# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 04:12:14 2017

@author: Vishaal Bommena
"""
import psycopg2
from random import randint
from sklearn import neighbors
from machine_learning_service import normalize, ml_train,  ml_distances
from operator import itemgetter

n_neighbors = 4
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')

def write(X, course_name, option):
    X_t = ()
    for i in range (0, len(X)):
        tuples = ()
        tuples = tuples + (i, )
        tuples = tuples + (course_name[i],)
        for j in range(0 , len(X[i])):
            tuples = tuples + (X[i][j], )
        X_t = X_t + (tuples,)
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        if (option == 0):
            cur.execute("DROP TABLE IF EXISTS studentList")
            cur.execute("CREATE TABLE studentList(Id Int PRIMARY KEY, C_Name text, Math Int, CritT Int, TW Int, SD Int, Mem Int, option Int)")
            query = ("INSERT INTO studentList(Id, C_Name, Math, CritT, TW, SD, MEM, option) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            cur.executemany(query, X_t)
            con.commit()
        if(option == 1):
            cur.execute("DROP TABLE IF EXISTS courseList")
            cur.execute("CREATE TABLE courseList(Id Int PRIMARY KEY, C_Name text, Math Int, CritT Int, TW Int, SD Int, Mem Int)")
            query = ("INSERT INTO courseList(Id, C_Name, Math, CritT, TW, SD, MEM) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cur.executemany(query, X_t)
            con.commit()
    finally:
        if con:
            con.close()

def read(option):
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()

        if (option == 0) :
            cur.execute("SELECT * FROM studentList")
            colnames = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            temp = []
            for row in rows:
                temp.append(list(row))
            reads = []
            options = []
            for i in range(0, len(temp)):
                temps = []
                for j in range(2, len(temp[i])-1):
                    temps.append(temp[i][j])
                options.append(temp[i][6])
                reads.append(temps)
            reads = normalize(reads, options)
            #print(colnames)
            return (reads)
        if (option == 1):
            cur.execute("SELECT * FROM courseList")
            colnames = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            temp = []
            for row in rows:
                temp.append(list(row))
            reads = []
            for i in range(0, len(temp)):
                temps = []
                for j in range(2, len(temp[i])):
                    temps.append(temp[i][j])
                reads.append(temps)
            #print(colnames)
            return (reads)
    finally:
        if con:
            con.close()

def clear(X, option):
    conn = None
    rows_deleted = 0
    try:
        conn = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = conn.cursor()
        if (option == 0):
            for i in range (1, 3):
                cur.execute("DELETE FROM course WHERE Id = %s", (str(i)))
                rows_deleted = rows_deleted + 1
            conn.commit()
            cur.close()
            #print(rows_deleted)
            #print(cur.rowcount)
    finally:
        if (conn is not None):
            conn.close()

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

def predict_data():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        cur.execute("SELECT trait FROM course")
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
        cur.execute(query)
        conn.commit()
        query = 'create table "{}"(ID INT NOT NULL PRIMARY KEY, name TEXT, score INT)'.format(str(uid))
        cur.execute(query)
        conn.commit()
        for i in range(0, len(names)):
            #print(names[i])
            querry = ('INSERT INTO "{}"(ID, name, score) VALUES (%s, %s, %s)'.format(str(uid)))
            cur.execute(querry, (i, names[i], scores[i]))
        conn.commit()
        cur.close()
    finally:
         if (conn is not None):
            conn.close()
