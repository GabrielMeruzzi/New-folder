import sqlalchemy as sqla

engine = sqla.create_engine('sqlite:///4-9 py tratamento erro sqlachemy/exercicio1/users.sqlite')

metadata = sqla.MetaData()

users_table = sqla.Table(
    'users', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('name', sqla.String),
    sqla.Column('age', sqla.Integer)
)

metadata.create_all(engine)

with engine.connect() as conn:
    with conn.begin():
        conn.execute(users_table.insert().values(name='Paulo', age=55))
        conn.execute(users_table.insert().values(name='Ana', age=35))
        conn.execute(users_table.insert().values(name='Fernanda', age=40))

try:
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(users_table.insert().values(id=1, name='Palo', age=60))
except sqla.exc.IntegrityError:
    print('errou')