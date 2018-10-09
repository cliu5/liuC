# LiuseLeef - Brian Lee, Claire Liu, Tim Marder
# SoftDev1 pd6
# K17 -- Average
# 2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def makeTable():
    #==========================================================
    c.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    c.execute("CREATE TABLE courses(id INTEGER, code TEXT, mark INTEGER)")

    with open("peeps.csv") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            # print(row["name"], row["age"], row["id"])
            command = "INSERT INTO students VALUES"
            command += "({}, \"{}\", {})".format(row["id"], row["name"], row["age"])
            c.execute(command)

    with open("courses.csv") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            # print(row["id"], row["code"], row["mark"])
            command = "INSERT INTO courses VALUES"
            command += "({}, \"{}\", {});".format(row["id"], row["code"], row["mark"])
            c.execute(command)
            #==========================================================
    db.commit() #save changes
    db.close()
