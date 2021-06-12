
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, create_engine
from sqlalchemy_utils import database_exists, create_database

# create db
def create_db():
    global engine
    engine = create_engine('postgresql://jswark:12345@localhost/new', echo=True)

    if not database_exists(engine.url):
        create_database(engine.url)

    global metadata
    metadata = MetaData(engine)

    return engine

def add_Table():
    class Author:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    class Book:
        def __init__(self, title, description, author):
            self.title = title
            self.description = description
            self.author = author

        def __repr__(self):
            return self.title

    authors_table = Table('authors', metadata,
                          Column('id', Integer, primary_key=True), Column('name', String))
    books_table = Table('books', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('title', String),
                        Column('description', String),
                        Column('author_id', ForeignKey('authors.id')))

    metadata.create_all(engine)  # creates the tables
    mapper(Book, books_table)
    mapper(Author, authors_table, properties = {
    'books': relation(Book, backref='author')})


    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    auth = Author('Aleksandr Semin 3')
    auth2 = Author('Aleksandr Semin 4')
    author_1 = Author('Richard Dawkins')
    author_2 = Author('Matt Ridley')
    book_1 = Book('The Red Queen', 'A popular science book', author_2)
    book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
    book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)

    session.add(author_1)
    session.add(author_2)
    session.add(book_1)
    session.add(book_2)
    session.add(book_3)
    session.add(auth)
    session.add(auth2)

    session.commit()
