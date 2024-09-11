import sqlalchemy as sqla 

engine = sqla.create_engine("sqlite:///28-8 py sqlalchemy e pandas/employees.sqlite")

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

with engine.connect() as conn:
    result = conn.execute(sqla.text("select * from users where age >= 55"))
    print(result.fetchall())

with engine.connect() as conn:
    q = sqla.select([users_table]).where(users_table.c.age > 50)
    result = conn.execute(q)