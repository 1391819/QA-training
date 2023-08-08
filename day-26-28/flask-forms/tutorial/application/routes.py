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

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f"Thank you, {first_name} {last_name}"

    return render_template("home.html", form=form, message=message)
