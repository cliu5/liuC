# LiuseLeef - Claire Liu, Brian Lee, Tim Marder
# SoftDev1 pd6
# K17 -- Average
# 2018-10-09

import sqlite3
import db_builder

def get_grades(id):
    '''
    Given a student id,
    returns a dictionary with courses as the keys and the student's grades as the values
    '''
    db = sqlite3.connect("discobandit.db")
    c = db.cursor()
    command = "SELECT code, mark FROM courses WHERE id=" + str(id)
    c.execute(command)
    grades = {}
    for grade in c:
        grades[grade[0]] = grade[1]
    return grades
    db.commit()
    db.close()

def get_average(id):
    '''
    Given a student id,
    returns their average
    '''
    grades = get_grades(id)
    total = 0
    for grade in grades:
        total += grades[grade]
    count = len(grades)
    if count == 0:
        return 0
    return total / count

def get_averages_all():
    '''
    Returns a list of tuples containing each student's ID, name, and their average.
    '''
    db = sqlite3.connect("discobandit.db")
    c = db.cursor()
    command = "SELECT * FROM students"
    c.execute(command)
    averages = []
    for student in c:
        # print(student)
        id = student[0]
        name = student[1]
        average = get_average(id)
        averages.append((id, name, average))
    return averages
    db.commit()
    db.close()

def print_averages():
    averages = get_averages_all()
    for average in averages:
        print("{}: {} has an average of {}".format(average[0], average[1], average[2]))

def create_averages_table():
    '''
    Creates a new table peeps_avg containing each student's id, name, and their average.
    '''
    db = sqlite3.connect("discobandit.db")
    c = db.cursor()
    command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, name TEXT, average DECIMAL)"
    c.execute(command)
    averages = get_averages_all()
    for average in averages:
        command = "INSERT INTO peeps_avg VALUES ({}, \"{}\", {})".format(average[0], average[1], average[2])
        c.execute(command)
    db.commit()
    db.close()

# print("Testing get_grades()")
# print(get_grades(4))
# print("Testing get_average()")
# print(get_average(4))
# print("Testing get_averages_all()")
# print(get_averages_all())
# print_averages()
db_builder.makeTable()
create_averages_table()
