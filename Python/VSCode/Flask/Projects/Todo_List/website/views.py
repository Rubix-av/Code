from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
def profile_redirect():
    return redirect(url_for("views.profile"))

@views.route("/profile")
@login_required
def profile():
    user_dict = {
    "email": current_user.email,
    "name": current_user.name,
    "age": current_user.age,
    "gender": current_user.gender,
    "date": current_user.date
    }
    
    return render_template("profile.html", user_dict=user_dict, user=current_user)

@views.route("/todo")
@login_required
def todo():
    return render_template("todo.html", user=current_user)
