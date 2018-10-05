#Team Haribo Gummy Bears - Claire Liu & Bo Hui Lu
#SoftDev1 pd6
#K #16: No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

studentdata = "CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,age INTEGER,userid INTEGER)"

c.execute(studentdata)#runs statement

coursedata= "CREATE TABLE courses(id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT, mark INTEGER, userid INTEGER)"

c.execute(coursedata)

#populates students table
with open('peeps.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        studentdata="INSERT INTO students(name, age, userid) VALUES ('"
        studentdata+= row['name'] + "', " + row['age'] + ", " + row['id']
        studentdata+= ");" 
        c.execute(studentdata)


#populates courses table
with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        coursedata="INSERT INTO courses(code, mark, userid) VALUES ('"
        coursedata+= row['code'] + "', " + row['mark'] + ", " + row['id']
        coursedata+= ");" 
        c.execute(coursedata)

        
#==========================================================

db.commit() #save changes
db.close() #close database
