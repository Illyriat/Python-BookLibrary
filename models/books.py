from models.book import *
import datetime

book1 = Book("The Lord of The Rings", "J.R.R Tolkien", "Fantasy", datetime.datetime(2021, 12, 15), True)
book2 = Book("A Game of Thrones", "George R.R Martin", "Fantasy", datetime.datetime(2021, 12, 15), False)
book3 = Book("Behind the Mask", "Tyson Fury", "Autobiography", datetime.datetime(2021, 12, 15), True)
book4 = Book("Cook and Share", "Mary Berry", "Food and Drinks", datetime.datetime(2021, 12, 15), False)

_books = [book1, book2, book3, book4]


def add_new_book(book):
    _books.append(book)

def delete_book(book_name):
    book_to_delete = None
    for book in _books:
        if book.title == book_name:
            book_to_delete = book
            break
    
    _books.remove(book_to_delete)