from application import app, db
from application.models import Countries, Cities

# create the database schema or even just test db connection
with app.app_context():
    db.drop_all()  # this should be removed if we don't want to delete existing data
    db.create_all()

    # add example to countries table
    uk = Countries(name="United Kingdom")
    db.session.add(uk)
    db.session.commit()

    # we reference the country that London belongs to using "country".
    # this is what we named the backref variable in db.relationship()
    ldn = Cities(name="London", country=uk)
    # this is the same as the above
    # difference is:
    #   we queried the table as if the Countries object had not been created in this session
    mcr = Cities(
        name="Manchester",
        country=uk
        # country=Countries.query.filter_by(name="United Kingdom").first(),
    )

    db.session.add(ldn)
    db.session.add(mcr)
    db.session.commit()

    # debug
    print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
    print(f"London's country is: {ldn.country.name}")
    print(f"Manchester's country is: {ldn.country.name}")
