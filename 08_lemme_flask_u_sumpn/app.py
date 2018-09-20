#Claire Liu
#SoftDev1 pd6
#K08 Fill Yer Flask
#2018-9-20


from flask import Flask #import flask
app = Flask(__name__) 

@app.route('/') #first route
def first():
    return '''whats shakin bacon!
           '''

@app.route('/alligator') #second route
def second():
    return '''
            see ya later alligator!
            '''

@app.route('/peel') #third route
def third():
    return '''whats the deal banana peel!
            '''


if __name__ == '__main__': #running flask
    app.debug = True
    app.run()
