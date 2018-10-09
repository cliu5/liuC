import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def login():
    if request.cookies.get('session'):
        return render_template("home.html")

@app.route('/login', methods=['POST'])

        return render_template('login.html', loginfailed = '')

@app.route('/login', methods=['POST'])
def auth():
    if request.form['usr'] == '1234':
        if request.form['pwd'] == '4321':
            session['usr'] = request.form['usr']
            return render_template('welcome.html', user = session['usr'])
        else:
            return render_template('login.html', loginfailed = "Wrong password")
    else:
        return render_template('login.html', loginfailed = "Wrong username")


@app.route('/logout')
def logout():
    session.pop('usr')
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.debug = True
    app.run()
