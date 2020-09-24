#!/usr/bin/python3
import os
from flask import Blueprint, render_template, redirect, url_for
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

if __name__ == '__main__':
    auth.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)