from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating Flask instance
app = Flask(__name__)

# creating SQLAlchemy connection
# we use sqlite in this case, no need for a .env file or dotenv
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# creating db object
db = SQLAlchemy(app)

# importing view functions after Flask instance creation
from application import routes
