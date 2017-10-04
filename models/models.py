from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# from app import db


app = Flask(__name__)

app.config["SECRET_KEY"] = "kennypro"

#directing API to databse yummy_recipes
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://startups:pass@localhost:5432/reci"

db = SQLAlchemy(app)

#User Model in SQL
class User(db.Model):

    # __table__ = "Users"

    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(60))
    password = db.Column(db.String(80))



    def __init__(self,id,username,email, password):
        #initiliazing User class constructor
        self.username=username
        self.email = email
        self.password = password
        self.id =id



    def __repr__(self):
        #method to return user information when querying database
        return "<User: %s>" % self.email



class Recipe(db.Model):

    # __table__ = "Recipes"

    recipe_id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(1000))
    id = db.Column(db.String(100))
    date_modified = db.Column(db.DateTime)



    def __init__(self,recipe_id,description,title,id,date_modified):
            #initiliazing User class constructor
        self.recipe_id=recipe_id
        self.title = title
        self.description=description
        self.id = id
        self.date_modified=date_modified


    def __repr__(self):
        #method for retuning data when querying database
        return "<Recipe: %s>" % self.title
