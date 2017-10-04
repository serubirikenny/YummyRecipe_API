from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models.models import User, app, db
#import jwt



# app = Flask(__name__)
#
# app.config["SECRET_KEY"] = "kennypro"
#
# #directing API to databse yummy_recipes
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://startups:pass@localhost:5432/reci"
#
# db = SQLAlchemy(app)

#-----------------------------------------------ROUTES/ENDPOINTS----------------------------------------------------

#Route for registering a user.This route takes the users details and assigns them a unique id
@app.route("/register",methods=["Post"])
def create_user():
    user_info = request.get_json()

    hashed_password = generate_password_hash(user_info["password"], method="sha256")

    new_user = User( id=str(uuid.uuid4()),username=user_info["username"], email=user_info["email"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message" : "New user  has been created!"})

#Route for obtaining all users in the database
@app.route("/registered_users",methods=["GET"])
def get_users():
    users = User.query.all()

    registered_users= []

    for user in users:
        user_data = {}
        user_data["username"] = user.username
        user_data["email"] = user.email
        user_data["password"] = user.password
        user_data["id"] = user.id
        registered_users.append(user_data)

    return jsonify({"users" : registered_users})

#Route to obtain an individual user in the databse using their id
@app.route("/registered_user/<id>" ,methods=["GET"])
def get_user(id):

    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({"message" : "No user found!"})

    user_data = {}
    user_data["username"] = user.username
    user_data["email"] =user.email
    user_data["password"] = user.password
    user_data["id"] = user.id

    return jsonify({"user" : user_data})



#Route to delete an individual user using their id
@app.route("/delete_registered_user/<id>",methods=["DELETE"])
def delete_user(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({"message" : "No user found!"})

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message" : "The user has been deleted!"})


"""
# #
# @app.route("")
# def


# #
# @app.route("")
# def


# #
# @app.route("")
# def

"""
#-----------------------------------------RUNNING APP-----------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
