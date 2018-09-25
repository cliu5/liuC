#Team Cucumber
#Claire Liu + Kaitlin Wan
#SoftDev1 PD6
#K #10: Jinja Tuning ...
#2018-09-24

from flask import Flask, render_template
from util import ants
app=Flask(__name__)

@app.route("/")
def helloWorld():
    return "go to /occupations"

@app.route("/occupations")
def occupations():
    #uses our template in /templates directory
    return render_template('template.html',randomJob=ants.randomJob(),jobs=ants.dictionaryMaker())

if (__name__ == "__main__"):
    app.debug = True
    app.run()
