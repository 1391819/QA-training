def get_books(author):
    # this is local to the function
    # shouldn't be here in the long term?
    books_and_authors = {
        "J.R.R. Tolkien": ["Lord of the Rings"],
        "J.K. Rowling": [
            "Harry Potter 1",
            "Harry Potter 2",
            "The Hobbit",
        ],
        "George Orwell": ["Animal Farm", "1984"],
    }

    # use entered author and return all his/her books as a list
    books = books_and_authors.get(author, [])

    return books


# get user input
author = input("Enter author name: ")

# get needed books and sort
books = sorted(get_books(author))

# checking if there are any books by the specified author
if books:
    to_return = ", ".join(books)
    print("Here are the books: " + to_return)
else:
    print("No books by the specified author")
