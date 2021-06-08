import sqlalchemy as sql
from sqlalchemy.orm import mapper, relation

# создать классы для таблиц
class Author(object):
    def init (self, name):
        self.name = name
    def repr (self):
        return self.name

class Book(object):
    def init (self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def repr (self):
        return self.title

engine = sql.create_engine('sqlite:///:memory:', echo=False)

metadata = sql.MetaData() #- Штука которая позволяет строить SQLalchemy Table objects
authors_table = sql.Table('authors', metadata,
                sql.Column('id', sql.Integer, primary_key=True), sql.Column('name', sql.String))
books_table = sql.Table('books', metadata,
            sql.Column('id', sql.Integer, primary_key=True),
            sql.Column('title', sql.String),
            sql.Column('description', sql.String),
            sql.Column('author_id', sql.ForeignKey('authors.id')))
metadata.create_all(engine)	# creates the tables

print(engine.table_names())

# мэппим классы с таблицами
mapper(Book, books_table)
mapper(Author, authors_table, properties = {'books': relation(Book, backref='author')})

# raw sql query
cursor = engine.connect()
query = '''
select *
from authors
where id >=2
'''
result = cursor.execute(query)
print(result)
print(list(result))
