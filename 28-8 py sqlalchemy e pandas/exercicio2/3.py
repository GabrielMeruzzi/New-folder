import sqlalchemy as sqla 

engine = sqla.create_engine("sqlite:///vendas.sqlite")

metadata = sqla.MetaData()

table_vendas = sqla.Table(
    'vendas', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('produto', sqla.String),
    sqla.Column('quantidade', sqla.Integer),
    sqla.Column('valor_unitario', sqla.Integer)
)

metadata.create_all(engine)

with engine.connect() as conn:
    with conn.begin():
        conn.execute(table_vendas.insert().values(produto='Shampoo', quantidade=5, valor_unitario=10))

with engine.connect() as conn:
    result = conn.execute(sqla.text("select * from vendas"))
    print(result.fetchall())
