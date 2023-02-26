from fastapi import FastAPI

app = FastAPI()

@app.get('/books')
async def get_all_books():
    pass

@app.get('/books/{book_id}')
async def get_book_by_id(book_id: int):
    pass

@app.post('/books')
async def add_book():
    pass

@app.put('/books/{book_id}')
async def update_book(book_id: int):
    pass

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    pass