# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, Register


# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="TEST_SECRET_KEY",
            TESTING=True,
            DEBUG=True,
            WTF_CSRF_ENABLED=False,
        )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        sample1 = Register(name="MsWoman")
        # save users to database
        db.session.add(sample1)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()


# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"MsWoman", response.data)


# Write a test class to rest Create functionality
class TestCreate(TestBase):
    def test_register_form_post(self):
        # sending post request
        response = self.client.post(
            url_for("home"), data=dict(name="Test Register"), follow_redirects=True
        )

        self.assert200(response)

        # checking if the entry got added to the db
        # this should be done with IDs, but in this case the primary key is the
        # name (never do this since names are not usually unique)
        obj1 = Register.query.filter_by(name="Test Register").first()
        assert obj1 is not None
        self.assertEqual(obj1.name, "Test Register")

        # checking that the correct template has been used
        self.assert_template_used("home.html")
