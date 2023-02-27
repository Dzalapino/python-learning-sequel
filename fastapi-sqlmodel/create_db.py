from sqlmodel import SQLModel
from models import Book
from db_engine import engine

print("CREATING DATABASE...")
SQLModel.metadata.create_all(engine)