#from config import auth
from sqlalchemy import create_engine

engine = create_engine('postgresql://jswark:12345@localhost/pockemons', echo=True)
cursor = engine.connect()

query = '''
select *
from authors
where id >=2
'''

query2 = '''
insert into authors
values (123 , 'ekkqweqweek') , (1231 ,'piasdkabu')
'''

result = cursor.execute(query)
print(result)
print(list(result))