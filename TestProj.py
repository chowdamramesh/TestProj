import os
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hack2hire'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


ed_user = User(id='123', username='rammi', email='eds@password')
db.session.add(ed_user)
db.session.commit()

@app.route('/user/<username>', methods=["GET", "POST"])
def hello_world(username):
    # user = User.query.all()
    if request.method == 'GET':
        try:
            
        except Exception as e:
            print("Failed to add book")
            print(e)
    return "Hello"

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()
