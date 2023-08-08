from application import app, db
from application.models import Games
from flask import render_template


@app.route("/")
def index():
    all_games = Games.query.all()
    number_of_games = Games.query.count()

    return render_template(
        "index.html", games=all_games, number_of_games=number_of_games
    )


@app.route("/add")
def add() -> str:
    """Add endpoint: add a new game to the database

    Returns:
        str: Confirmation message
    """
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return render_template("add.html", game=new_game)


@app.route("/read")
def read() -> str:
    """Read endpoint: see all the games in the database

    Returns:
        str: String representation of the game
    """
    all_games = Games.query.all()

    return render_template("read.html", games=all_games)


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

    return render_template("update.html", game=first_game)


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

    return render_template("delete.html", game=game_to_delete)
