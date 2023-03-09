from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
bcrypt = Bcrypt(app)


from market import routes