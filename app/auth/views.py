from flask import render_template,redirect,url_for,request,flash
from .import auth
from ..import db 
from ..models import User
from flask_login import login_user,logout_user,login_required,current_user
from werkzeug.security import generate_password_hash,  check_password_hash


@auth.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email ).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('main.home'))
            else:
                flash('password is incorrect',category='error')
        else:
            flash('Email does not exist!',category='error')
    return render_template('auth/login.html',user = current_user)
@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists=User.query.filter_by(email= email).first()
        username_exists = User.query.filter_by(username = username).first()

        if email_exists:
            flash('Email is already in use , use another email.',category='error')

        elif username_exists:
            flash('Username is already in use, try a different user.',category='error')

        elif password1 != password2:
            flash("password don\'t match!" ,category="error")

        elif len(username)<7:
            flash("username is too short,Must have 7 characters and above.", category ="error")
        elif len(password1)<8:
            flash("password  is too short,Password must be 8 character and above.", category ="error")

        elif len(email)<10:
            flash("Email is invalid,Must have 10 characters and above", category='error')

        else:
            new_user = User(email = email,username=username,password= generate_password_hash(password1,method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('User created successfuly')
            return redirect(url_for("main.home"))




    return render_template("auth/signup.html",user= current_user)
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))