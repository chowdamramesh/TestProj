import os
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
import json
from flask.json import JSONEncoder
from sqlalchemy import func
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hack2hire'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Financial_goals(db.Model):
				id = db.Column(db.Integer, primary_key=True)
				loan =  db.Column(db.Integer)
				lifestyle =  db.Column(db.Integer)
				education =  db.Column(db.Integer)

class Acc_summary(db.Model):
    id = db.Column(db.Integer)
    trx_id = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    ref = db.Column(db.String(120))
    credit = db.Column(db.Integer)
    debit = db.Column(db.Integer)
    trx_date = db.Column(db.Date)

class Account_details(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(80))
    acc_num = db.Column(db.String(120))
    acc_balance = db.Column(db.Integer)
    

class PredictTerm(db.Model):
				age = db.Column(db.Integer)
				job = db.Column(db.String(80))
				marital = db.Column(db.String(80))
				education = db.Column(db.String(80))
				default_a = db.Column(db.String(80))
				housing = db.Column(db.String(80))
				loan = db.Column(db.String(80))
				contact = db.Column(db.String(80))
				month = db.Column(db.String(80))
				day_of_week = db.Column(db.String(80))
				duration = db.Column(db.Integer)
				campaign = db.Column(db.Integer)
				pdays = db.Column(db.Integer)
				previous = db.Column(db.Integer)
				poutcome = db.Column(db.String(80))
				emp_var_rate = db.Column(db.Integer)
				cons_price_idx = db.Column(db.Integer)
				cons_conf_idx = db.Column(db.Integer)
				euribor3m = db.Column(db.Integer)
				nr_employed = db.Column(db.Integer)
				id = db.Column(db.Integer , primary_key=True)




# ed_user = User(id='123', username='rammi', password='password')
# Financial_goals(id = '123',loan = , lifestyle = , education = )
# db.session.add(ed_user)
# db.session.commit()
ma = Marshmallow(app)
class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id','trx_id','ref','credit','debit','trx_date')

account_share_schema = AccountSchema(many=True)

class AccountDetailSchema(ma.Schema):
    class Meta:
        fields = ('id','name','acc_num','acc_balance')

account_share_schema = AccountSchema(many=True)
account_Dshare_schema = AccountDetailSchema(many=True)

@app.route('/login', methods=['POST'])
def login():
    # we don't need to check the request type as flask will raise a bad request
    # error if a request aside from POST is made to this url

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    print(user.password)
    print(password)

    if user.password == password and user.username == username:
        return jsonify(id=user.id,username=username, status='OK'  )
    else:
        return jsonify(status='NO')


@app.route('/accountSummary', methods=['GET','POST'])
def accountSummary():
    acc_id = request.form['id']
    accSummary= Acc_summary.query.filter_by(id=acc_id).all()
    result = account_share_schema.dump(accSummary)
    return jsonify(result.data)

@app.route('/accountDetails', methods=['GET','POST'])
def accountDetails():
    acc_id = request.form['id']
    accDSummary= Account_details.query.filter_by(id=acc_id).first()
    # result = account_Dshare_schema.dump(accDSummary)
    return jsonify(name = accDSummary.name , acc_num = accDSummary.acc_num , acc_balance = accDSummary.acc_balance)


@app.route('/setFinancialGoals', methods=['POST'])
def financial_goals():
    acc_id = request.form['id']
    loan = request.form['loan']
    lifestyle = request.form['lifestyle']
    education = request.form['education']
    fd_user = Financial_goals(id = acc_id,loan = loan, lifestyle = lifestyle, education = education)
    db.session.add(fd_user)
    db.session.commit()
    return jsonify(status = '200')


@app.route('/termDeposit', methods=['GET','POST'])
def getTermDeposit():
    acc_id = request.form['id']
    return jsonify (flag='NO')


if __name__ == '__main__':
    app.run()
app.debug(True)
