from application import app
from application import library
from classes.book import Book
from flask import request


@app.route("/")
@app.route("/home")
def index():
    # display all books

    if library.books:
        return [str(book) for book in library.books]
    else:
        return "There are no books currently in the library"


@app.route("/add")
def add_book():
    # add new books with information supplied via url/query params

    # examples
    # /add?title=Title&pages=200&isbn=1231231231231&genre=Fantasy

    """
    /add?title=ToKillaMockingbird&pages=336&isbn=978-0061120084&genre=Fiction&author=HarperLee
    /add?title=1984&pages=328&isbn=978-0451524935&genre=Fiction&author=GeorgeOrwell
    /add?title=AnimalFarm&pages=328&isbn=123123123&genre=Fiction&author=GeorgeOrwell
    /add?title=PrideandPrejudice&pages=432&isbn=978-0141439518&genre=Classic&author=JaneAusten
    /add?title=TheGreatGatsby&pages=180&isbn=978-0743273565&genre=Fiction&author=F.ScottFitzgerald
    /add?title=TheCatcherintheRye&pages=240&isbn=978-0316769488&genre=Fiction&author=J.D.Salinger
    /add?title=HarryPotterandtheSorcerer'sStone&pages=320&isbn=978-0590353427&genre=Fantasy&author=J.K.Rowling
    /add?title=ToAlltheBoysI'veLovedBefore&pages=384&isbn=978-1442426702&genre=YoungAdult&author=JennyHan
    /add?title=TheLordoftheRings:TheFellowshipoftheRing&pages=432&isbn=978-0618346257&genre=Fantasy&author=J.R.R.Tolkien
    /add?title=TheHungerGames&pages=384&isbn=978-0439023528&genre=YoungAdult&author=SuzanneCollins
    /add?title=TheDaVinciCode&pages=592&isbn=978-0307474278&genre=Mystery&author=DanBrown

    """

    title = request.args.get("title")
    pages = request.args.get("pages")
    isbn = request.args.get("isbn")
    genre = request.args.get("genre")
    author = request.args.get("author")

    if not title or not pages or not isbn or not genre:
        return "Missing required parameters"

    # TODO: Add isbn validation
    # has_valid_isbn = Book.check_isbn(isbn)
    # if not has_valid_isbn:
    #    return "Please enter a correct ISBN", 400

    if not author:
        book = Book(title, pages, isbn, genre)
    else:
        book = Book(title, pages, isbn, genre, author)

    library.add_book(book)

    return "Book added to the library"


@app.route("/search/<string:author>")
def search_book(author: str):
    # search for books by a given author

    # example
    # /search/Bobby

    author_books = library.search_books_by_author(author)

    if author_books:
        return [str(book) for book in author_books]
    else:
        return "There are no books by the specified author"


@app.route("/update/<string:isbn>")
def update_book(isbn: str):
    # update books that have already been added based on isbn

    # example
    # /update/978-0307474278?title=new_title&pages=1&isbn=123&genre=new_genre&author=fake_author

    new_title = request.args.get("title")
    new_pages = request.args.get("pages")
    new_isbn = request.args.get("isbn")
    new_genre = request.args.get("genre")
    new_author = request.args.get("author")

    if (
        not new_title
        and not new_pages
        and not new_isbn
        and not new_genre
        and not new_author
    ):
        return "You must specify at least one parameter to update"

    if library.update_book(
        isbn=isbn,
        new_title=new_title,
        new_pages=new_pages,
        new_isbn=new_isbn,
        new_genre=new_genre,
        new_author=new_author,
    ):
        return "Book updated successfully"

    return "Book was not found in the library!"


@app.route("/delete/<string:isbn>")
def delete_book(isbn: str):
    # delete books from the system based on title

    # example
    # /delete/1231233

    if library.remove_book(isbn):
        return "Book removed from library"

    return "Book was not found in the library"
