from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


class UserCheck:
    def __init__(self, banned, special_characters, message=None):
        self.banned = banned
        self.special_characters = special_characters
        if not message:
            message = "Please choose another username"
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

        if any(char in self.special_characters for char in field.data):
            self.message = "Username must not include special characters"
            raise ValidationError(self.message)


class myForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            UserCheck(
                message="That username is not allowed",
                banned=["root", "admin", "sys"],
                special_characters=" !\#$%&'()*+,/:;<=>?@[\]^`{|}~",
            ),
            Length(min=2, max=15),
        ],
    )
    submit = SubmitField("Sign up")


@app.route("/", methods=["GET", "POST"])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template("home.html", form=form, username=username)
    else:
        return render_template("home.html", form=form, username="")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
