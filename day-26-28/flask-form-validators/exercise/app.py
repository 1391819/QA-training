# imports
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import os
from dotenv import load_dotenv

# creating flask object
app = Flask(__name__)

# loading env variables and configuring CSRF protection
load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


# custom WTForm validator
class UserCheck:
    def __init__(self, banned, special_characters, message=None):
        self.banned = banned
        self.special_characters = special_characters
        if not message:
            message = "Please choose another username"
        self.message = message

    def __call__(self, form, field):
        # if entered username is same as any of the words contained in self.banned
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

        # if entered username contaisn any of the special characters defined in self.special_characters
        if any(char in self.special_characters for char in field.data):
            self.message = "Username must not include special characters"
            raise ValidationError(self.message)


# Form class
class myForm(FlaskForm):
    # username string
    username = StringField(
        "Username",
        validators=[
            DataRequired(),  # in-built validator
            # custom validator, using the UserCheck class
            UserCheck(
                message="That username is not allowed",
                banned=["root", "admin", "sys"],
                special_characters=" !\#$%&'()*+,/:;<=>?@[\]^`{|}~",
            ),
            # in-built validator
            Length(min=2, max=15),
        ],
    )
    # sign up button
    submit = SubmitField("Sign up")


# basic route to display and retrieve data from the form
@app.route("/", methods=["GET", "POST"])
def postName():
    # instantiate form
    form = myForm()
    # check if all validators have been validated on submission
    if form.validate_on_submit():
        username = form.username.data
        return render_template("home.html", form=form, username=username)
    else:
        return render_template("home.html", form=form, username="")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
