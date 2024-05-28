from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home():
    dict = {
    "email": current_user.email,
    "name": current_user.name,
    "age": current_user.age,
    "gender": current_user.gender,
    "date": current_user.date
    }
    return render_template("home.html", user_dict=dict, user=current_user)
