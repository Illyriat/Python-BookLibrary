from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.books import _books, delete_book

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index2():
    return render_template("index.html")

@app.route('/books')
def books():
    return render_template("books.html", title="Book List", books=_books)

@app.route('/books', methods=['POST'])
def add_book():
    print(request.form)
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']

    newBook = Book(title, author, genre)
    print(newBook.__dict__)
    _books.append(newBook)

    return redirect('/books')

@app.route('/books/delete/<string:title>', methods=['POST'])
def delete_book_button(title):
    delete_book(title)
    print(_books)
    return redirect('/books')