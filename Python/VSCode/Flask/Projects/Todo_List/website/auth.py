from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import db, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint("auth", __name__)

# Login page backend
@auth.route("/login", methods=["GET","POST"])
def login():
    user_dict = {}
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Login successfull!", category='success')
                return redirect(url_for("views.profile"))
            else:
                flash("Incorrect password!", category='error')
                return redirect(url_for("auth.login"))
        else:
            flash("User doesn't exist!", category='error')
            return redirect(url_for("auth.login"))
        
        user_dict = {
                "email": user.email,
                "name": user.name,
                "age": user.age,
                "gender": user.gender,
                "date": user.date
            }
    return render_template("login.html", user_dict=user_dict, user=current_user)

# Sign-Up page backend
@auth.route("/sign-up", methods=["GET","POST"])
def sign_up():
    user_dict = {}
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = Users.query.filter_by(email=email).first()

        if user:
            flash("User already exists!", category='error')
            return redirect(url_for("auth.sign_up"))
        elif len(name) < 2:
            flash("Name must be greater than 2 letters!", category='error')
            return redirect(url_for("auth.sign_up"))
        elif age < 18:
            flash("Age must be greater than 18!", category='error')
            return redirect(url_for("auth.sign_up"))
        elif gender == "":
            flash("Select a gender!", category='error')
            return redirect(url_for("auth.sign_up"))
        elif password1 != password2:
            flash("Incorrect password!", category='error')
            return redirect(url_for("auth.sign_up"))
        else:
            new_user = Users(email=email, name=name, age=age, gender=gender, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user, remember=True)
            flash("User created successfully", category='success')
            return redirect(url_for("views.profile"))
        
        user_dict = {
            "email": email,
            "name": name,
            "age": age,
            "gender": gender,
            "date": user.date
        }
    return render_template("sign-up.html", user_dict=user_dict, user=current_user)

@auth.route("logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", category='success')
    return redirect(url_for("auth.login"))

