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
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name, dashboard_data=mongo.db.logs.find())



#log=mongo.db.log.find()

