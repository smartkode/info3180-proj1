from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wrzoerdkpbgaeh:ExE09bAKJpCL0zrZbMdoKfL77c@ec2-23-21-96-129.compute-1.amazonaws.com:5432/d466s8ob9kv9av'
app.config['SECRET_KEY']='sjddjhdgjdshdghjsvdn'

db = SQLAlchemy(app)
from app import views
