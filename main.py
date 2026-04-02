from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


books = [
    {
        'id': 1,
        'title' : 'Broke',
        'author' : 'fatima Rala',
        'publisher' : 'pratdeep singha',
        'published_date': '02-04-05',
        'page count' : 2300,
        'language': 'Francais'
    },
    {
        'id': 2,
        'title' : 'As far as the lemon tea grows',
        'author' : 'fatimata sillah',
        'publisher' : 'preeta sanyang',
        'published_date': '01-04-15',
        'page count' : 1300,
        'language': 'Espanol'
    },
{
        'id': 3,
        'title' : 'A thousand yellow sun',
        'author' : 'chima achebe',
        'publisher' : 'singh omar',
        'published_date': '24-04-25',
        'page count' : 3000,
        'language': 'portuguese'
    },
{
        'id': 4,
        'title' : 'NOVEMBER 4TH',
        'author' : 'COLA HOVIN',
        'publisher' : 'prithvi singh',
        'published_date': '03-03-03',
        'page count' : 6000,
        'language': 'Anglaise'
    },
{
        'id': 5,
        'title' : 'It starts with us',
        'author' : 'COLA HOVIN',
        'publisher' : 'prithvi singh',
        'published_date': '06-03-06',
        'page count' : 4500,
        'language': 'chinese'
    },
{
        'id':6,
        'title' : 'It ends with us',
        'author' : 'COLA HOVIN',
        'publisher': 'prithvi singh',
        'published_date': '09-03-09',
        'page count' : 4000,
        'language': 'Korean'
    }
]

class Book(BaseModel):
    id:int
    title : str
    author: str
    publisher : str
    published_date : str
    page_count : int
    language : str

class BookUpdateModel(BaseModel):
    title : str
    author: str
    publisher : str
    page_count : int
    language : str

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books',status_code= status.HTTP_201_CREATED)
async def get_all_books(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book    

@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'book not found')

@app.patch('/book/{book_id}')
async def update_book(book_id:int, book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] == book_update_data.title
            book['publisher'] == book_update_data.publisher
            book['page_count'] == book_update_data.page_count
            book['language'] == book_update_data.language
            return book
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail='book not found')

@app.get('/book/{book_id}')
async def delete_book(book_id:int) -> dict:
    pass




    













