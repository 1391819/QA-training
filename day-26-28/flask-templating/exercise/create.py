from application import app, db

# create schema/test connection
with app.app_context():
    db.drop_all()  # this should be removed if we don't want to delete existing data
    db.create_all()
