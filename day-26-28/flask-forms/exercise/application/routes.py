from application import app
from application.models import BasicForm
from flask import render_template, request


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def register():
    message = ""
    form = BasicForm()

    if request.method == "POST":
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        favourite_number = form.favourite_number.data
        favourite_food = form.favourite_food.data

        if (
            len(first_name) == 0
            or len(last_name) == 0
            or dob is None
            or favourite_number is None
            or favourite_food is None
        ):
            message = "Please supply all the data"
        else:
            message = f"Thank you, {favourite_food}-{first_name}-{dob}-{favourite_number}-{last_name}"

    return render_template("home.html", form=form, message=message)
