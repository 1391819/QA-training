from application import app
from flask import redirect, url_for
from werkzeug.wrappers import Response


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
