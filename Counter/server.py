
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets, secrets'

@app.route('/')
def count():
    if 'count' in session:
        session['count'] = session.get ('count') + 1
    else:
        session['count'] = 1
    return render_template('counter.html', count = session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")

@app.route('/addtwo')
def addtwo():
    session['count'] += 2
    return render_template ('counter.html')

    
if __name__=="__main__": 
    app.run(debug=True) 