from flask import Flask, render_template, request
from flask import session

import pymysql as sql

app = Flask(__name__)

def connect():
    srvr = sql.connect(host='localhost', port=3306, user='root', password='', database='portfolio')
    cur = srvr.cursor()
    return srvr,cur

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/aftersubmit/', methods = ['GET', 'POST'] )
def aftersubmit():
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        message = request.form.get('message')
        srvr, cur = connect()
        cmd1 = f"select * from details where email = '{email}'"
        cur.execute(cmd1)
        data1 = cur.fetchall()
        if data1:
            msg1 = "Email already Exists....."
            return render_template('contact.html', data= msg1)
        else:
            cmd = f"insert into details values('{name}', '{email}', '{number}', '{message}')"
            cur.execute(cmd)
            srvr.commit()
            srvr.close()
            msg = "Your details is stored in our servers....."
            return render_template('contact.html', data= msg)

app.run(debug=True)