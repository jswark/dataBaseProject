#from config import auth
from sqlalchemy import create_engine


#engine = create_engine('postgresql://{}:{}@localhost/sqlachemy_db'.format(auth['user'], auth['password']), echo=True)
engine = create_engine('sqlite:///:memory:', echo=False)
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