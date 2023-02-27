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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return result

@app.post('/books')
async def add_book():
    pass

@app.put('/books/{book_id}')
async def update_book(book_id: int):
    pass

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    pass