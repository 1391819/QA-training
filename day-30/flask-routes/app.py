# A basic web app that uses routes to provide a /home and an /about page.

"""
    Check your terminal and take note of how Flask logs all incoming HTTP requests to the app while it's running

    127.0.0.1 - - [07/Aug/2023 12:27:08] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [07/Aug/2023 12:27:25] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [07/Aug/2023 12:27:29] "GET /home HTTP/1.1" 200 -
    127.0.0.1 - - [07/Aug/2023 12:27:39] "GET /about HTTP/1.1" 200 -
"""

from flask import Flask

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
