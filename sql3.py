#from config import auth
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
schema_name = 'example3'


#engine = create_engine('postgresql://{}:{}@localhost/sqlachemy_db'.format(auth['user'], auth['password']), echo=True)
engine = create_engine('sqlite:///:memory:', echo=False)
# metadata = MetaData(engine)
engine.execute('CREATE SCHEMA IF NOT EXISTS {}'.format(schema_name))


class Author(Base):
    __tablename__ = 'authors'
    __table_args__ = {'schema': schema_name}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    __table_args__ = {'schema': schema_name}

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey(Author.id))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) # bound session
session = Session()
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
# or simply session.add_all([author_1, author_2, book_1, book_2, book_3])
session.commit()
book_3.description = u'The theory of evolution' # update the object
print(book_3 in session )# check whether the object is in the session

session.commit()