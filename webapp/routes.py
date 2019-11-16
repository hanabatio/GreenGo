from flask import render_template, flash, redirect, url_for, request
from webapp import app, db
from sqlalchemy import update
#from webapp.forms import *
#from webapp.models import *

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)