# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:11:27 2017

@author: Vishaal Bommena
"""
import psycopg2
from random import randint

def clear(i):
    conn = None
    rows_deleted = 0
    try: 
        conn = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
        cur = conn.cursor()
        i = str(i)
        cur.execute("DELETE FROM student WHERE uid = %s", (i, ))
        rows_deleted = rows_deleted + 1
        print("rows deleted: ", rows_deleted)
        conn.commit()
        cur.close()
    finally: 
        if (conn is not None):
            conn.close()

def write(C, opt):
    course = ()
    course = course + (C, )
    print("courses: ", course)
    if (opt == 0):
        try:
            con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
            cur = con.cursor()
            query = ("INSERT INTO course(idcourse, name, description, professor, upvote, timings, trait) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cur.executemany(query, course)
            con.commit()
        finally:
            if con:
                con.close()
    if (opt == 1):
        uid = 2
        username = "smouli"
        name = "Sanat"
        #taken_course = "cs182"
        #options = "11"
        taken_course = ["cs182", "cs180", "cs240", "ma161"]
        options = [11, 11, 12, 13]
        temp = (str(uid), str(username), str(name), taken_course, options, )
        print("temp: ", temp)
        cr = ()
        cr = cr + (temp, )
        print ("cr: ", cr)
        try:
            con = psycopg2.connect(host = 'ec2-54-163-229-169.compute-1.amazonaws.com', database = 'df5g8vla4snv52', user = 'yipgikbasudyog', password = '21d1ee6803375e19da2ed3cfc8c726f036e3e11871d62b65df13134be5c69ec2')
            cur = con.cursor()
            query = "INSERT INTO student(uid, username, name, taken_course, option) VALUES (%s, %s, %s, %s, %s)"
            cur.executemany(query, cr)
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

def add_course(id_stud, course_name):
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
        else: 
            return "Course Exists!!"
        
        C = reads[0][2]
        cur.execute("update student SET taken_course = %s WHERE uid = %s", (C, str(id_stud), ))
        con.commit()
        
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
        finally:
             if (conn is not None):
                conn.close()
        return "done"
    return "error"


def testing():
    #print(create(0))
    inputs = []
    #file = 'Course_data.txt'
    '''
    with open(file) as f:
        inputs = f.readlines()
    temp = []
    for i in range(0, len(inputs)):
        temp.append([line for line in [line.strip() for line in inputs[i].split("\"")] if line])
    courses = temp    
    C = ()
    for i in range(0, len(courses)):
        X = ()
        for j in range(0, len(courses[i])):
            traits = []
            if (j == len(courses[i]) - 1):
                traits = courses[i][j].split(" ")
                X = X + (traits, )
            else: 
                X = X + (courses[i][j], )
        C = C + (X, )
        '''
    #name_table()
    #for i in range(0, 15):
    #    clear(i)
    #read()
    #for i in range (0, len(C)):
    #    write(C[i], 0)
    #print(read())
    #write(C, 1)
    #print("Adding Course: ", add_course(str(1), "cs182"))
    print("Adding Course: ", add_course(str(105825808192854652718), "ENTR200"))
testing()
