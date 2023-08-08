from application import app, db
from application.models import Games


@app.route("/add")
def add() -> str:
    """Add endpoint: add a new game to the database

    Returns:
        str: Confirmation message
    """
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"


@app.route("/read")
def read() -> str:
    """Read endpoint: see all the games in the database

    Returns:
        str: String representation of the game
    """
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>" + game.name
    return games_string


@app.route("/update/<name>")
def update(name) -> str:
    """Update endpoint: update the name of the first entry in the games table

    Args:
        name (str): New name

    Returns:
        str: Updated name
    """
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name


# done like this simply because that was the task specification
# in a real world scenario, you always want to have control over what you are deleting
# e.g., -> pass an URL parameter (id) and use .query.filter_by(id=id).first()
@app.route("/delete")
def delete() -> str:
    """Delete endpoint: delete the first entry in the database

    Returns:
        str: Confirmation message
    """
    game_to_delete = Games.query.first()
    db.session.delete(game_to_delete)
    db.session.commit()

    return "Delete first entry game from the database"


@app.route("/get_number_of_games")
def get_number_of_games() -> str:
    """Return the amount of games present in the database

    Returns:
        str: Message
    """
    number_of_games = Games.query.count()

    return f"There are {number_of_games} in the database"
