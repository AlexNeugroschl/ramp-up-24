from fastapi import FastAPI
import book

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