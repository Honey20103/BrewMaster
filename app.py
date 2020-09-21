#!/usr/bin/python3
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'brew_master'
app.config["MONGO_URI"] = 'mongodb+srv://root:rootbabyboy@honeycluster.v8y4e.mongodb.net/brew_master?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_base')
def test():
    return render_template("/flask_auth_app/project/base.html", base=mongo.db.log.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
