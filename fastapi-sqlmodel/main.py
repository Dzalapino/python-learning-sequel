from fastapi import FastAPI, status, HTTPException
from models import Book
from db_engine import engine
from sqlmodel import Session, select
from typing import List

# init fastapi
app = FastAPI()

session = Session(bind=engine)

@app.get('/books', response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    query = select(Book)
    result = session.exec(query).all()
    return result

@app.get('/books/{book_id}', response_model=Book)
async def get_book_by_id(book_id: int):
    query = select(Book).where(Book.id==book_id)
    result = session.exec(query).one_or_none()
    
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id=} doesn't exist.")
    
    return result

@app.post('/books', response_model=Book, status_code=status.HTTP_201_CREATED)
async def add_book(book: Book):
    new_book = Book(title=book.title, description=book.description)
    
    session.add(new_book)
    session.commit()

    return new_book

@app.put('/books/{book_id}', response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book):
    query = select(Book).where(Book.id==book_id)
    book_to_update = session.exec(query).one_or_none()
    
    if book_to_update == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id=} doesn't exist.")

    book_to_update.title = book.title
    book_to_update.description = book.description
    session.commit()

    return book_to_update

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    query = select(Book).where(Book.id==book_id)
    result = session.exec(query).one_or_none()

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id=} doesn't exist.")
    
    session.delete(result)
    
    return result