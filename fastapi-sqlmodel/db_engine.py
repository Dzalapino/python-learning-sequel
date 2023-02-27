from sqlmodel import SQLModel, create_engine
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
CONNECTION_STR = 'sqlite:///' + os.path.join(BASE_DIR, 'books.db')

engine = create_engine(CONNECTION_STR, echo=True)