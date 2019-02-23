import os
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
import json
from flask.json import JSONEncoder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hack2hire'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Acc_summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trx_id = db.Column(db.String(80), unique=True, nullable=False)
    ref = db.Column(db.String(120))
    credit = db.Column(db.Integer)
    debit = db.Column(db.Integer)



# ed_user = User(id='123', username='rammi', password='password')
# db.session.add(ed_user)
# db.session.commit()


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

# app.json_encoder = MyJSONEncoder

@app.route('/accountSummary', methods=['GET','POST'])
def accountSummary():
    acc_id = request.form['id']
    accSummary= Acc_summary.query.filter_by(id=acc_id).all()

    # print(accSummary[0])
    # return jsonify(data=accSummary)
    # return jsonify(my_dict)
    return jsonify(eqtls={e.serialize() for e in accSummary})
    # return json.dumps(accSummary, default=json_util.default)


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, EqltByGene):
            return {
                'id': obj.gene_id, 
                'trx_id': obj.trx_id,
                'ref':obj.ref,
                'credit':obj.credit,
                'debit': obj.debit,
            }
        return super(MyJSONEncoder, self).default(obj)

class EqltByGene(object):
    def serialize(self):
        return {
            'id': self.gene_id, 
            'trx_id': self.gene_trx_id,
            'ref': self.gene_ref,
            'credit': self.credit,
            'debit':self.debit
        }

if __name__ == '__main__':
    app.run()
app.debug(True)