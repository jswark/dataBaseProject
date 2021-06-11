
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, create_engine

engine = create_engine('postgresql://jswark:12345@localhost/pockemons', echo=True)


metadata = MetaData()

authors_table = Table('authors', metadata,
                      Column('id', Integer, primary_key=True), Column('name', String))
books_table = Table('books', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

metadata.create_all(engine)  # creates the tables

insert_stmt = authors_table.insert(bind=engine)
print(insert_stmt)
compiled_stmt = insert_stmt.compile()
print(compiled_stmt.params)
insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries

metadata.bind = engine # no need to explicitly bind the engine from now on
select_stmt = authors_table.select(authors_table.columns.id==2)
print(select_stmt)
result = select_stmt.execute()
print("lolkek", result.fetchall())

upd_stmt = authors_table.update().where(authors_table.c.id==2).values(name="Lol Kekov")
upd_stmt.execute()
del_stmt = authors_table.delete()
del_stmt.execute(whereclause=text("name='Mr Y'"))
del_stmt.execute()

for t in metadata.sorted_tables:
    print(t.name)