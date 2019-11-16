from flask import render_template, flash, redirect, url_for, request
from webapp import app, db
from sqlalchemy import update
from webapp.forms import *
from webapp.models import *

default_goal = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    form = registrationForm(request.form)
    if form.validate_on_submit():
       
        user = User(username=form.email.data, name= form.name.data, password= form.password.data,
        goal= default_goal, totalEmissions=0, currEmissions=0, lastTrip=0)
        db.session.add(user)
        db.session.commit()

        flash(f'Account Created','success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods= ['GET', 'POST'])
def logIn():
    form = logInForm(request.form)
    #do something

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)