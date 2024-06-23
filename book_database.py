from sqlalchemy import MetaData, create_engine, Integer, String, Float, ForeignKey, Column
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import pyodbc

DRIVER = "ODBC Driver 17 for SQL Server"
SERVERNAME = "DESKTOP-499EAJ9"
INSTANCENAME = "\SQLEXPRESS"
DB = "db_ai_bookstore_5_1_ryan_b"

metadata = MetaData()  # Create the metadata variable.
engine = create_engine(f"mssql+pyodbc://{SERVERNAME}{INSTANCENAME}/{DB}?driver={DRIVER}", connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()  # Start the db_session so that the data can be queried from book_database.


# Table for books.
class Book(Base):
    __tablename__ = 'tbl_book'  # Point to the books table.
    # Set all of the columns to their specific variables for books.
    col_pk_book_id = Column(Integer, primary_key=True)
    col_book_title = Column(String)
    col_book_summary = Column(String)
    col_book_genre = Column(String)
    col_book_text = Column(String)
    col_fk_author_id = Column(Integer, ForeignKey('tbl_author.col_pk_author_id'))
    author_data = relationship("Author", backref="tbl_book", primaryjoin="Book.col_fk_author_id == Author.col_pk_author_id", foreign_keys="Book.col_fk_author_id")


# Table for author details.
class Author(Base):
    __tablename__ = 'tbl_author'  # Point to the book_details table.
    # Set all of the columns to their specific variables for book_details.
    col_pk_author_id = Column(Integer, primary_key=True)
    col_author_first_name = Column(String)
    col_author_last_name = Column(String)
    col_ai_author = Column(Integer)
    # book_id = Column(ForeignKey('books.book_id'))


# Table for author details.
class User(Base):
    __tablename__ = 'tbl_user'  # Point to the book_details table.
    # Set all of the columns to their specific variables for book_details.
    col_pk_user_id = Column(Integer, primary_key=True)
    col_username = Column(String)
    col_user_first_name = Column(String)
    col_user_last_name = Column(String)


# Table for author details.
class Review(Base):
    __tablename__ = 'tbl_review'  # Point to the book_details table.
    # Set all of the columns to their specific variables for book_details.
    col_pk_review_id = Column(Integer, primary_key=True)
    col_fk_book_id = Column(Integer, ForeignKey('tbl_book.col_pk_book_id'))
    col_fk_reviewer_id = Column(Integer, ForeignKey('tbl_user.col_pk_user_id'))
    col_stars = Column(Integer)
    col_review_text = Column(String)
    book_data = relationship("Book", backref="tbl_review", primaryjoin="Review.col_fk_book_id == Book.col_pk_book_id", foreign_keys="Review.col_fk_book_id")
    user_data = relationship("User", backref="tbl_review", primaryjoin="Review.col_fk_reviewer_id == User.col_pk_user_id", foreign_keys="Review.col_fk_reviewer_id")


# Retrieving data from the database
def get_books():  # Query all of the book details from the Book table above.
    return db_session.query(Book)

def get_authors():  # Query all of the book details from the Book table above.
    return db_session.query(Author)


def get_users():  # Query all of the book details from the Book table above.
    return db_session.query(User)


def get_reviews():  # Query all of the book details from the Book table above.
    return db_session.query(Review)


# Retrieving book data from the database
def get_specific_book(id):  # Query specific book details from the Book table above based on the id the user chose.
    return db_session.query(Book).filter_by(col_pk_book_id=id).all()


def get_specific_author(id):  # Query specific book details from the Book table above based on the id the user chose.
    return db_session.query(Author).filter_by(col_pk_author_id=id).all()


def get_specific_user(id):  # Query specific book details from the Book table above based on the id the user chose.
    return db_session.query(User).filter_by(col_pk_user_id=id).all()


def get_specific_review(id):  # Query specific book details from the Book table above based on the id the user chose.
    return db_session.query(Review).filter_by(col_fk_book_id=id).all()


# Retrieving data from the database
# def get_book_details(id):  # Query specific book details from the BookDetails table above based on the id the user chose.
    # return db_session.query(BookDetails).filter_by(col_pk_book_id=id).all()