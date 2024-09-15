from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import db, User
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=["GET","POST"])

def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if password == user.password:
                login_user(user, remember=True)
                flash('Login successfull!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password! Try Again", category='danger')
        else:
            flash("User doesn't exist!", category='danger')

    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        age = int(request.form.get('age'))
        hobby = request.form.get('hobby')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("User already exists!", category='danger')
        elif len(email) < 4:
            flash("Email must be greater than 4 letters!", category='danger')
        elif len(name) < 2:
            flash("Name is too short!", category='danger')
        elif age < 18:
            flash("You aren't eligible!", category='danger')
        elif len(hobby) <= 2:
            flash("Hobby must be greater than 2 characters!", category='danger')
        elif password1 != password2:
            flash("Incorrect passwords!", category='danger')
        else:
            new_user = User(email=email, name=name, age=age, hobby=hobby, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            return redirect(url_for("views.home"))
        
    return render_template("sign-up.html", user=current_user)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", category='success')
    return redirect(url_for("auth.login"))


