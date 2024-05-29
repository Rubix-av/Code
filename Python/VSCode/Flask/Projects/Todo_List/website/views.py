from flask import Blueprint, render_template, redirect, url_for, request, flash
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

    # checks if todo exists
    existing_todo = Todo.query.filter_by(user_id=current_user.id).all()
    todo_exists = existing_todo if existing_todo else ""

    # checks if request method is POST
    if request.method=="POST":
        title = request.form.get("todoTitle")
        desc = request.form.get("todoDesc")

        if not title:
            flash("Add a title!", category='error')
            return redirect(url_for("views.todo"))
        if not desc:
            flash("Add a description!", category='error')
            return redirect(url_for("views.todo"))      
        
        else:
            new_todo = Todo(title=title, desc=desc, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()

            allTodo = Todo.query.filter_by(user_id=current_user.id).all()

            # Adds more todos in front of our already existing todo
            flash("Todo added successfully!", category='success')
            return render_template("todo.html", user=current_user, allTodo=allTodo)

    # todo_exists is replaced with existing_todo if it exists else with ""
    return render_template("todo.html", user=current_user, allTodo=todo_exists)
        
