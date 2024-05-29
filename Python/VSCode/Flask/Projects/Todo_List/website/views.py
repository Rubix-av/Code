from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .model import db, Users, Todo

views = Blueprint("views", __name__)


@views.route("/")
def profile_redirect():
    return redirect(url_for("views.profile"))

@views.route("/profile")
@login_required
def profile():
    user_dict = {
    "id": current_user.id,
    "email": current_user.email,
    "name": current_user.name,
    "age": current_user.age,
    "gender": current_user.gender,
    "date": current_user.date
    }
    
    return render_template("profile.html", user_dict=user_dict, user=current_user)

@views.route("/todo", methods=["GET","POST"])
@login_required
def todo():
    if request.method=="POST":
        title = request.form.get("todoTitle")
        desc = request.form.get("todoDesc")

        new_todo = Todo(title=title, desc=desc, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for("views.todo"))

    return render_template("todo.html", user=current_user)
