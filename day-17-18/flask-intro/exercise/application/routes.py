from application import app
from random import choice


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

    return f"{choice(first_name_list)} {choice(last_name_list)}"
