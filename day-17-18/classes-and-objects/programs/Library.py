from Book import Book


class Library:
    def __init__(self, books: list[Book] = []) -> None:
        self.books = books

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def search_book(self, book: Book) -> None:
        if book in self.books:
            print(book)
        else:
            print("Book is not in our library.")

    def search_books_by_author(self, author: str) -> list[Book]:
        books_by_author = []

        for book in self.books:
            if book.search(author):
                books_by_author.append(book)

        return books_by_author
