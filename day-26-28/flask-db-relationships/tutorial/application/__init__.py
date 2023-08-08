# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# creating Flask instance
app = Flask(__name__)

# creating SQLAlchemy connection

# loading environment variables
# this is also used by flask's .run() behind the scenes
# TODO: Search how it used and if this load_dotenv() call is needed
load_dotenv()

# retrieving environment variables from .env file
DB_TYPE = os.getenv("DB_TYPE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# stand-alone database - MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = (
    DB_TYPE + DB_USER + DB_PASSWORD + DB_HOST + DB_NAME
)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# built-in database - sqlite
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# this is creating a simulation of the database as an object in our application
db = SQLAlchemy(app)

# import models
import application.models

# importing create to perform db related stuff
import application.create

# importing view functions after Flask instance creation
import application.routes
