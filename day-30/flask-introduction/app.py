# A basic app that displays a message saying Hello internet!.

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello_internet():
    return "Home"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
