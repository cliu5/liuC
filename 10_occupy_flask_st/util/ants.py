#From Claire Liu's HW 2:
#Uses more robust code + is easier to follow
from random import choice
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
        key.strip('"')
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
