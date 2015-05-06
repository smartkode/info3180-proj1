from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///postgres'
app.config['SECRET_KEY']='sjddjhdgjdshdghjsvdn'

db = SQLAlchemy(app)
from app import views
