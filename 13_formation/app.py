#Claire Liu
#SoftDev1 pd06
#K13: Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def helloworld():
	return render_template("first.html")

@app.route("/auth")
def auth():
	return render_template("template.html", username = request.args["username"], method = request.method)

if __name__ == "__main__":
	app.debug = True;
	app.run()
