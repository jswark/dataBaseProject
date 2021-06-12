from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey, text, create_engine, insert

engine = create_engine('postgresql://postgres:12345@localhost/postgres', echo=True)


metadata = MetaData()

pokedex_table = Table('pokedex', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name_rus', String, nullable=False, index = True),
                      Column('name_eng', String, nullable=False),
                      Column('element', String, ForeignKey('elements.element'), nullable=False),
                      Column('type', String, nullable=False),
                      Column('height', Float, nullable=False),
                      Column('weight_type', Integer, ForeignKey('health.weight_type'), nullable=False))

health_table = Table('health', metadata,
                     Column('weight_type', Integer, primary_key=True),
                     Column('health', Integer, nullable=False))

elements_table = Table('elements', metadata,
                       Column('element', String, primary_key=True),
                       Column('attack', Integer, nullable=False),
                       Column('total', Integer, nullable=False))

metadata.create_all(engine)  # creates the tables

# data
pokemons = [[1,'Бульбазавр','Bulbasaur','травяной','зерно',0.7,1],
        [2,'Чармандер', 'Charmander', 'огненный', 'ящерица', 0.6, 3],
        [3, 'Сквиртл', 'Squirtle', 'водный','черепаха', 0.5, 3]]

health = [[1,500],
          [2,750],
          [3,1000]]

elements = [['травяной',77],
            ['огненный',69],
            ['водный',80],
            ['электрический',71],
            ['обычный',60]]

count={'травяной':0,'огненный':0,'водный':0,'электрический':0,'обычный':0}

for i in pokemons:
    insert_stmt = (insert(pokedex_table).values(id=i[0], name_rus=i[1], name_eng=i[2], element=i[3], type=i[4],
                                   height=i[5], weight_type=i[6]))
    compiled_stmt = insert_stmt.compile()

for i in health:
    insert_stmt = (insert(health_table).values(weight_type=i[0], health=i[1]))
    compiled_stmt = insert_stmt.compile()

for i in pokemons:
    count[i[3]]+=1

for i in elements:
    insert_stmt = (insert(elements_table).values(element=i[0], attack=i[1], total=count[i[0]]))
    compiled_stmt = insert_stmt.compile()
