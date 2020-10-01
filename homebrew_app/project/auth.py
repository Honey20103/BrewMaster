#!/usr/bin/python3
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from bson.objectid import ObjectId
from . import mongo

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # first check if the user actually exists
    # take the inputted password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please try again, credentials seem to be wrong.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.dashboard'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Try to query the db to validate if user already exists, if it returns user than user exists.
    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect them back to signup page so user can try again
        flash('It seems you are already a member')
        return redirect(url_for('auth.signup'))

    # create a new user with the form model db structure. Added password hash to prevent plaintext display.
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # adding the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/cancel')
@login_required
def cancel():
    if current_user is None:
        return redirect(url_for('index'))
    try:
        db.session.delete(current_user)
        db.session.commit()
    except:
        return 'unable to delete the user.'
    return render_template('cancel.html')

@auth.route('/addlog', methods=["GET", "POST"])
@login_required
def addlog():
    if request.method == "POST":
        log = {
            "recipe_name": request.form.get("recipe_name"),
            "brew_date": request.form.get("brew_date"),
            "duration": request.form.get("duration"),
            "alcohol": request.form.get("alcohol"),
            "ingredients": request.form.get("ingredients"),
            "mashing": request.form.get("mashing"),
            "lautering": request.form.get("lautering"),
            "boiling": request.form.get("boiling"),
            "cooling": request.form.get("cooling"),
            "fermentation": request.form.get("fermentation"),
            "maturing": request.form.get("maturing"),
        }
        mongo.db.logs.insert_one(log)
        flash("Log Successfully Added")
        return redirect(url_for("main.dashboard"))
    return render_template('addlog.html')


@auth.route("/edit_log/<log_id>", methods=["GET", "POST"])
@login_required
def edit_log(log_id):
    if request.method == "POST":
        update = {
            "recipe_name": request.form.get("recipe_name"),
            "brew_date": request.form.get("brew_date"),
            "duration": request.form.get("duration"),
            "alcohol": request.form.get("alcohol"),
            "ingredients": request.form.get("ingredients"),
            "mashing": request.form.get("mashing"),
            "lautering": request.form.get("lautering"),
            "boiling": request.form.get("boiling"),
            "cooling": request.form.get("cooling"),
            "fermentation": request.form.get("fermentation"),
            "maturing": request.form.get("maturing"),
        }
        mongo.db.logs.update({"_id": ObjectId(log_id)}, update)
        flash("Log Successfully Updated")

    the_log = mongo.db.log.find_one({"_id": ObjectId(log_id)})
    return render_template('edit_log.html', log=the_log)
