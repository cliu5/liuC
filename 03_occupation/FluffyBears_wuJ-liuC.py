#Fluffy Bears -- Jeffrey Wu and Claire Liu
#SoftDev1 pd6
#K06 - StI/O: Divine your Destiny!
#2018-09-13

from random import choice

def dictionaryMaker():
    dictionary = {}
    file = open('occupations.csv','r')
    straw = file.read()
    lines = straw.split("\n")
    #delete useless lines
    del lines[0]
    del lines[-1]
    for line in lines:
        #sets comma to last comma (only relevant)
        comma=line.rfind(",")
        #before comma = key, after = val
        key =line[:comma]
        val = line[comma+1:]
        dictionary[key] = val
    return dictionary

def randomJob():
    jobs = dictionaryMaker()
    #weightedJobs will store reps of jobs
    weightedJobs = []
    for jobKey in jobs:
        #weight -> freq of each job given by percentage
        weight = float(jobs[jobKey]) * 10
        #adds correct number of reps to list
        weightedJobs += [jobKey,] * int(weight)
    return choice(weightedJobs)

print(randomJob())
