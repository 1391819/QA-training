from application import app, db
from application.models import Users

# create the database schema or even just test db connection
with app.app_context():
    db.drop_all()  # this should be removed if we don't want to delete existing data
    db.create_all()

    # creating a testing user
    testuser = Users(first_name="Roberto", last_name="Nacu")
    db.session.add(testuser)
    db.session.commit()
