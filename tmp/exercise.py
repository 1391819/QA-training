"""

Write a random name generator which allows a user to generate a random firstname + lastname 
combination

"""
from random import randint
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    name = random_generator()

    return name


def random_generator():
    """Generate a random first name + last name

    Returns:
        str: String representation of random full name
    """
    first_name_list = ["Roberto", "Amy", "Sarah", "Mark", "John"]
    last_name_list = ["Nacu", "Robinsons", "Smith", "Johnson"]

    return f"{first_name_list[randint(0, len(first_name_list) - 1)]} {last_name_list[randint(0, len(last_name_list) - 1)]}"


if __name__ == "__main__":
    app.run(debug=True)
