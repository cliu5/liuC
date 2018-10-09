# Claire Liu
# SoftDev1 pd06
# K#00 
# yyyy-mm-dd

from flask import Flask
app = Flask(__name__) 

@app.route("/")      
def hello_world():
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run()
