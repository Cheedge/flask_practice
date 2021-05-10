from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from model import User, Post
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# app a Flask class instance
app = Flask(__name__)

app.config['SECRET_KEY'] = '6ee30fca55ef434eb1e0d0401637c1cb'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes
