"""
Create a class Book. Each book object should have the attributes: 
    - title
    - author (default unknown) 
    - number of pages
    - genre
    - ISBN
    
The class should define the following methods:
    - __init__ to set the attributes described above
    - __str__ to print a description of the book
    - a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
    - a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise

As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
"""


class Book:
    def __init__(
        self,
        title: str,
        pages: int,
        isbn: str,
        genre: str,
        author: str = "Unknown",
    ) -> None:
        """Initialise book instance and set attributes

        Args:
            title (str): Title of the book
            pages (int): Number of pages of the book
            isbn (str): ISBN of the book
            genre (str): Genre of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.isbn = isbn

    def __str__(self):
        return (
            f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.pages}"
            + f"\nGenre: {self.genre}\nISBN: {self.isbn}"
        )

    """
    A static method is a method that belongs to the class itself and does not depend on the instance of the class. Unlike regular instance methods that have access to instance-specific data, static methods only have access to the arguments passed to them and other static attributes or methods within the class.    
    
    You should use @staticmethod in Python when you have a method in a class that:

        - Does not require access to the instance (no self parameter needed).
        - Performs a task that is related to the class, but not to any specific instance.
        - Doesn't rely on or modify any instance-level attributes or state.
    """

    @staticmethod
    def check_isbn(isbn: str) -> bool:
        """Determine the validity of a given ISBN

        Args:
            isbn (str): ISBN to check for validity

        Returns:
            bool: True if the isbn is valid, False otherwise.
        """

        # remove special characters (-) and whitespaces
        isbn = isbn.replace("-", "")
        isbn = isbn.strip()  # just in case

        # raise errors in case of invalid isbns
        if len(isbn) != 13:
            raise (ValueError("ISBN must contain 13 digits"))

        # get check digit
        check_digit = int(isbn[-1])
        # remove check digit from isbn
        isbn = isbn[:-1]

        sum = 0

        # go through the whole ISBN
        for idx, char in enumerate(isbn):
            # alternating weights
            if idx % 2 == 0:
                tmp_sum = int(char) * 1
            else:
                tmp_sum = int(char) * 3

            # adding to sum
            sum += tmp_sum

        # checking if check_digit is valid or not
        if (sum + check_digit) % 10 == 0:
            return True
        else:
            return False

    def search(self, author):
        if self.author == author:
            return True
        else:
            return False


if __name__ == "__main__":
    # creating books
    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )

    book2 = Book(
        "Dark Matter",
        352,
        "978-1101904220",
        "Science Fiction, Thriller",
        "Blake Crouch",
    )

    book3 = Book(
        "Educated: A Memoir",
        352,
        "978-0399590504",
        "Memoir, Autobiography",
        "Tara Westover",
    )

    book4 = Book(
        "Circe",
        400,
        "978-0316556347",
        "Fantasy, Mythology",
        "Madeline Miller",
    )

    book5 = Book(
        "The Silent Patient",
        336,
        "978-1250301697",
        "Psychological Thriller",
        "Alex Michaelides",
    )

    # printing book info
    print(book1)

    # checking isbn
    print(book1.check_isbn("978-1416550549"))

    # creating library - very simple for now
    library = [book1, book2, book3, book4, book5]

    # searching for a particular author's books
    author = "Alex Michaelides"
    author_books = []

    # searching books written by the requested author
    for book in library:
        if book.search(author):
            author_books.append(book)

    # printing books by the requested author
    for book in author_books:
        print(book)
