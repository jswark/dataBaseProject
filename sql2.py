
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, create_engine



engine = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData(engine)
books_table = Table('books', metadata, autoload=True) # create a Table object
authors_table = Table('authors', metadata, autoload=True) # create a Table object


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


mapper(Book, books_table)
mapper(Author, authors_table, properties = {
'books': relation(Book, backref='author')})


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
auth = Author('Aleksandr Semin 3')
auth2 = Author('Aleksandr Semin 4')
session.add(auth)
session.add(auth2)
session.commit()
