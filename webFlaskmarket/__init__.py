from flask import Flask, render_template



from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECRET_KEY'] = '8759bcc0393cbd49058cd644'
db=SQLAlchemy(app)

from .base_models import Item
from webFlaskmarket import routes
