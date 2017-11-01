# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 04:12:14 2017

@author: Vishaal Bommena
"""
import psycopg2
from random import randint
from sklearn import neighbors
from machine_learning_service import normalize, ml_train, ml_predict

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

def name_table():
    con = None
    try:
        con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = con.cursor()
        cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        print (cur.fetchall())
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
            print(rows_deleted)
            print(cur.rowcount)
    finally:
        if (conn is not None):
            conn.close()

def training(train_data, clf):
    ml_train(train_data, clf)

def predicts(predict_data, clf):
    ml_predict(predict_data, clf)

def testing():
    train_data = []
    user_number = 9
    for i in range (0, user_number):
        lists = []
        for j in range (0, 5):
            if (i < 4):
                lists.append(randint(0, 5))
            if (i >=4 and i < 9):
                lists.append(randint(6, 10))
        train_data.append(lists)

    for i in range(0, len(train_data)):
        if (i < 3):
            train_data[i].append(13)
        if (i >= 3 and i < 7):
            train_data[i].append(12)
        if (i >= 7 and i < 9):
            train_data[i].append(11)

    course_name = []
    for i in range (0, user_number):
        string = "cs25"
        string = string + str(i)
        course_name.append(string)

    #User Data
    name_table()
    write(train_data, course_name, 0)
    norm_data = read(train_data, 0)
    #print(norm_data)
    ml_train(norm_data, clf)

    #Prediction
    pred_data = []
    for i in range (0, 20):
        lists = []
        for j in range (0, 5):
            lists.append(randint(0, 10))
        pred_data.append(lists)



    course_name = []
    for i in range (0, 20):
        string = "Me25"
        string = string + str(i)
        course_name.append(string)

    #Total Course List
    write(pred_data, course_name, 1)
    predict_data = read(1)
    #print(predict_data)
    prediction = ml_predict(predict_data, clf)
    for i in range(0, len(prediction)):
        if (prediction[i] == 0):
            print("Yes: ", predict_data[i])
        else:
            print("No: ", predict_data[i])

#testing()
