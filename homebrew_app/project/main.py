#!/usr/bin/python3
from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Claudette's testing"

@main.route('/profile')
def profile():
    return 'Profile'
