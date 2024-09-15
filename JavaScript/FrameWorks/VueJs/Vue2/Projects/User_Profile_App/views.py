from flask import jsonify, render_template_string, render_template, request
from flask_security import auth_required, current_user, roles_required, SQLAlchemyUserDatastore
from flask_security.utils import hash_password, verify_password
from extensions import db

def create_view(app, user_datastore : SQLAlchemyUserDatastore):

    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/user-login', methods=["POST"])
    def user_login():

        # store the json object inside "data" as python dict.
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # checks if there was no email or password entered
        if not email or not password:
            return jsonify({"message": "not valid email or password"}), 404
        
        # tries to obtain user with the email passed to this endpoint
        user = user_datastore.find_user(email=email)

        # if user doesn't exist, then returns an error
        if not user:
            return jsonify({"message": "invalid user"}), 404
        
        # checks password for the email and returns json object with status code 200
        if verify_password(password, user.password):
            return jsonify({"token": user.get_auth_token(), 'role': user.roles[0].name, "id": user.id, "email": user.email}), 200

    @app.route('/register', methods=["POST"])
    def register():

        # stores the json object sent to this route in "data" as a python dict.
        data = request.get_json()
        
        # retrievs email & password from data dict.
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not email or not password or role not in ['inst','stud']:
            return jsonify({"message": "invalid input"})
        
        if user_datastore.find_user(email=email):
            return jsonify({"message": "user already exists"})

        # inst active = False
        if role == "inst":
            active = False
        elif role == "stud":
            active = True

        try:
            user_datastore.create_user(email=email, password=hash_password(password), roles=[role], active=active)
            db.session.commit()
        except:
            print("error while creating")
            db.session.rollback()
            return jsonify({"message": "error while creating user"}), 408
        
        return jsonify({"message": "user created"}), 200

    # profile
    @app.route('/profile')
    @auth_required('token')
    def profile():
        return render_template_string(
            """
                <h1>This is profile page</h1>
                <p> Welcome, {{current_user.email}} </p>
                <a href="/logout">logout</a>
            """
        )
    
    @app.route('/inst-dashboard')
    @roles_required('inst')
    def inst_dashboard():
        return render_template_string(
            """
                <h1>Instructor Profile</h1>
                <p>It should only be visible to instrcutor</p>
            """
        )

