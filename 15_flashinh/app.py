#Claire Liu and Tianrun Liu - Liu Squared
#SoftDev1 pd6
#K15 -- Oh yes, perhaps I do…
#2018-10-03

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(8)

@app.route('/')
def home():
    print("xxx DIAG:app xxx")
    print(app)
    print("xxx DIAG:request xxx")
    print(request)
    print("xxx DIAG:args xxx")
    print(request.args)
    print("xxx DIAG:form xxx")
    print(request.form)
    print("xxx DIAG:session xxx")
    print(session)
    #checks if there is a session
    if "username" in session:
        #if there is then just show the welcome screen
        return render_template('welcome.html',user = session['username'])
    else:
        #if not just ask for info
        return render_template('home.html')

@app.route('/login')
def login():
    #Login: Alan Smith PW: password12345678, checks if it is correct
    if request.args['usr'] == 'Alan Smith' and request.args['pwd']=='password12345678':
        print("xxx DIAG:args xxx")
        print(request.args)
        print("xxx DIAG:form xxx")
        print(request.form)
        session['username'] = "Alan Smith"
        print("xxx DIAG:session xxx")
        print(session)
        return redirect(url_for('home'))
    # if either is wrong then it returns an error message
    elif request.args['usr'] == 'Alan Smith' and request.args['pwd']!='password12345678':
        flash("password wrong")
        print("xxx DIAG:flash xxx")	
        print(flash)
        return render_template('home.html')
    else:
        flash("username wrong")
        return render_template('home.html')

@app.route('/logout')
def logout():
    #removes current session
    session.pop('username',"Alan Smith")
    print("xxx DIAG:session xxx")
    print(session)
    return redirect(url_for('home'))

	
if __name__ == "__main__":
    app.run(debug=True)
