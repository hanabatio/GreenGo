from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SECRET_KEY'] = 'u12z0JM7yg8lBhrxEertBUwobq8F86zA'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Junior7898@localhost/postgres'
db = SQLAlchemy(app)


from webapp import routes