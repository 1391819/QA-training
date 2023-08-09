from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# for now we put it here, use env variables please
app.config["SECRET_KEY"] = "extremely secret"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)
    password = db.Column(db.String(30), nullable=False)


class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        person = Register(
            name=request.form.get("name"),
            password=bcrypt.generate_password_hash(
                request.form.get("password").decode("utf-8")
            ),
        )
        db.session.add(person)
        db.session.commit()

    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data

        # this should be done with an id, not a name
        obj = Register.query.filter_by(name=name).first()

        # if name not found in the db
        if obj is None:
            return render_template("login.html", form=form, logged_in="Not logged in!")

        # else, the name is found, need to check passwords hash
        # we need to pass stored_hash and form password
        logged = bcrypt.check_password_hash(obj.password, password)

        if logged == True:
            return render_template(
                "login.html", form=form, logged_in="Successfully logged in!"
            )
        else:
            return render_template("login.html", form=form, logged_in="Not logged in!")
    else:
        return render_template("login.html", form=form, logged_in="Not logged in!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
