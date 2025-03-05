from flask import Blueprint, render_template, request, redirect
from datetime import datetime

from models.book import Book
from models.books import _books, delete_book


# Create a Blueprint instead of using `app`
controller = Blueprint('controller', __name__)

@controller.route('/')
def index():
    return render_template("index.html", title="Home")

@controller.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        checked_out = 'checked_out' in request.form  

        return_by = datetime.strptime(request.form['year'], '%Y-%m-%d') if checked_out and request.form['year'] else None

        newBook = Book(title, author, genre, return_by, checked_out)
        _books.append(newBook)

        return redirect('/books')

    return render_template("books.html", title="Book List", books=_books)


@controller.route('/books/delete/<string:title>', methods=['POST'])
def delete_book_button(title):
    delete_book(title)
    return redirect('/books')
