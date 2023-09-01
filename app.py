from flask import Flask, request, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db


## INSTALL ##
# pip3 install psycopg2-binary
# pip3 install flask-sqlalchemy

app = Flask(__name__)
# has to come before db variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
app.config['SECRET_KEY'] = 'garbanzo'

# app.app_context().push()

connect_db(app)
movies = db.session.execute("SELECT * FROM movies")
print(list(movies))

@app.route('/')
def home_page():
    return render_template("home.html")
