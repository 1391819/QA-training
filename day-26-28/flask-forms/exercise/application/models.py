from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField


class BasicForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    dob = DateField("Date of Birth")
    favourite_number = IntegerField("Favourite Number")
    favourite_food = SelectField(
        "Favourite food",
        choices=[("spaghetti", "Spaghetti"), ("pizza", "Pizza"), ("chilli", "Chilli")],
    )
    submit = SubmitField("Submit")
