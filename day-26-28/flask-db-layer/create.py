from app import db, app

# create the database schema
with app.app_context():
    db.create_all()
