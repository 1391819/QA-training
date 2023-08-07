from app import db, app

# create the database schema or even just test db connection
with app.app_context():
    db.create_all()
