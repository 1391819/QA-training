from flask import Flask, redirect, url_for
from werkzeug.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

app = Flask(__name__)


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

# built-in database - sqlite
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home() -> str:
    return "This is the home page"


@app.route("/about")
def about() -> str:
    return "This is the about page"


@app.route("/squared/<int:number>")
def squared(number: int) -> str:
    """Read a number in the URL (URL parameters/dynamic URL)

    Args:
        number (int): Number to be squared

    Returns:
        string: String displaying squared number
    """
    return f"Squared number is: {number**2}"


@app.route("/testing_redirect")
def testing_redirect() -> Response:
    return redirect(url_for("about"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
