from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey, text, create_engine, insert
from sqlalchemy.orm import mapper, relation
from sqlalchemy_utils import database_exists, create_database


from sqlalchemy import MetaData

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
    class PokedexClass:
        def __init__(self, id, name_rus, name_eng, elem, type, height, weight_t):
            self.id = id
            self.name_rus=name_rus
            self.name_eng = name_eng
            self.element = elem
            self.type= type
            self.height = height
            self.weight_type = weight_t

        def __repr__(self):
            return self.id

    class HealthClass:
        def __init__(self, weight, health):
            self.weight = weight
            self.health = health

        def __repr__(self):
            return self.weight

    class ElementClass:
        def __init__(self, element, attack, total):
            self.element = element
            self.attack = attack
            self.total=total

        def __repr__(self):
            return self.element

    pokedex_table = Table('pokedex', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('name_rus', String, nullable=False, index=True),
                          Column('name_eng', String, nullable=False),
                          Column('element', ForeignKey('elements.element'), nullable=False),
                          Column('type', String, nullable=False),
                          Column('height', Float, nullable=False),
                          Column('weight_type', ForeignKey('healths.weight'), nullable=False))

    health_table = Table('healths', metadata,
                         Column('weight', Integer, primary_key=True),
                         Column('health', Integer, nullable=False))

    elements_table = Table('elements', metadata,
                           Column('element', String, primary_key=True),
                           Column('attack', Integer, nullable=False),
                           Column('total', Integer, nullable=False))

    metadata.create_all(engine)  # creates the tables

    mapper(PokedexClass, pokedex_table )
    mapper(HealthClass, health_table, properties = {'healths': relation(PokedexClass, backref='weight_t')})
    mapper(ElementClass, elements_table, properties = {'elements': relation(PokedexClass, backref='elem')})

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    # data
    pokemons = [[1, '????????????????????', 'Bulbasaur', '????????????????', '??????????', 0.7, 1],
                [2, '??????????????????', 'Charmander', '????????????????', '??????????????', 0.6, 3],
                [3, '??????????????', 'Squirtle', '????????????', '????????????????', 0.5, 3]]

    health = [[1, 500],
              [2, 750],
              [3, 1000]]

    elements = [['????????????????', 77],
                ['????????????????', 69],
                ['????????????', 80],
                ['??????????????????????????', 71],
                ['??????????????', 60]]

    count = {'????????????????': 0, '????????????????': 0, '????????????': 0, '??????????????????????????': 0, '??????????????': 0}

    for i in pokemons:
        count[i[3]]+=1

    for i in health:
        exists = session.query(HealthClass).filter_by(weight = i[0]).first()
        if not exists:
            pokem = HealthClass(i[0], i[1])
            session.add(pokem)

    for i in elements:
        exists = session.query(ElementClass).filter_by(element=i[0]).first()
        if not exists:
            pokem = ElementClass(i[0], i[1], count[i[0]])
            session.add(pokem)

    for i in pokemons:
        exists = session.query(PokedexClass).filter_by(id = i[0]).first()
        if not exists:
            pokem = PokedexClass(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            session.add(pokem)

    session.commit()
