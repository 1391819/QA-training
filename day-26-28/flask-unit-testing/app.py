from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)


class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)


class RegisterForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        # this is not tested simply because we do not send
        # a post request to actually make this part of the code execute
        person = Register(name=form.name.data)
        with app.app_context():
            db.session.add(person)
            db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
