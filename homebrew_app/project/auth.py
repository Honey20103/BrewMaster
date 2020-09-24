#!/usr/bin/python3
import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Try to query the db to validate if user already exists, if it returns user than user exists.
    user = User.query.filter_by(email=email).first() 

    if user: # if a user is found, we want to redirect them back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form model db structure. Added password hash to prevent plaintext display.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # adding the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'

if __name__ == '__main__':
    auth.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)