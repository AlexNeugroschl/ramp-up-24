from fastapi import FastAPI
from book import Book

app = FastAPI() 

books = {}

@app.get('/{name}') 
async def say_hi(name:str):
    return {'message' : f"hello, {name}"}

@app.post('/books/')
async def add_book(book:book.Book):
    newID = len(books.keys) + 1
    books[newID] = book
    return book

@app.get('/books/')
def get_books():
    return books.values

@app.get('/books/{id}')
def get_book(id:int):
    return books[id]

@app.put('/books/{id}')
def update_book(id:int, book:book.Book):
    books[id] = book
    return books

@app.delete('/books/{id}')
def delete_book(id:int):
    del books[id]
    return books

