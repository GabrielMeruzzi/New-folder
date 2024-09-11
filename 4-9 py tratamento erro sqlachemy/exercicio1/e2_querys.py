import sqlalchemy as sqla
from sqlalchemy import exc

engine = sqla.create_engine('sqlite:///4-9 py tratamento erro sqlachemy/exercicio1/users.sqlite')

metadata = sqla.MetaData()

with engine.connect() as connection:
    with connection.begin():
        connection.execute(sqla.text("""
            drop table users;
        """))
        connection.execute(sqla.text("""
            create table if not exists users (
                id integer primary key autoincrement,
                nome varchar(30),
                idade int
            )
        """))
        connection.execute(sqla.text("""
            insert into users (nome, idade)
            values
                ('Joao', 20),
                ('Fernanda', 30),
                ('Thiago', 19),
                ('Gabriel', 21);
        """))
        
        try:
            connection.execute(sqla.text("""
            insert into users (id, nome, idade)
            values
                (1, 'Pola', 32);
        """))
        except sqla.exc.IntegrityError as e:
            print('Deu erro')