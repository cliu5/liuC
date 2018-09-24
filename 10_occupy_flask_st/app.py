#Team Cucumber
#Claire Liu + Kaitlin Wan
#SoftDev1 PD6
#K #10: Jinja Tuning ...
#2018-09-24

from flask import Flask, render_template
from random import choice
app=Flask(__name__)

#From Claire Liu's HW 2:
#Uses more robust code + is easier to follow
def dictionaryMaker():
    dictionary = {}
    file = open('data/occupations.csv','r')
    straw = file.read()
    lines = straw.split("\n") #seperates file
    #delete useless lines
    del lines[0]
    del lines[-1]
    del lines[-1]

    for line in lines:
        #sets comma to last comma (only relevant)
        comma=line.rfind(",")
        #before comma = key, after = val
        key = line[:comma]
        val = line[comma+1:]
        dictionary[key] = val #creates new key for each value
    return dictionary

#randomly selected occupation shown at the top
def randomJob():
    jobs = dictionaryMaker() #job is set to dictinary of occupations
    #weightedJobs will store reps of jobs
    weightedJobs = []
    for jobKey in jobs:
        #weight -> freq of each job given by percentage
        weight = float(jobs[jobKey]) * 10
        #adds correct number of reps to list
        weightedJobs += [jobKey,] * int(weight)
    return choice(weightedJobs)

@app.route("/")
def helloWorld():
    return "go to /occupations"

@app.route("/occupations")
def occupations():
    #uses our template in /templates directory
    return render_template('template.html',randomJob=randomJob(),jobs=dictionaryMaker())

if (_name_ == "_main_"):
    app.debug = True
    app.run()
