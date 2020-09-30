#!/usr/bin/python3
import os
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from . import db, mongo



main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@main.route('/get_log')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

#@main.route('/add_log')
#@login_required
#def add_log():
 #   return render_template(addlog.html)

#log=mongo.db.log.find()

if __name__ == '__main__':
    main.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)