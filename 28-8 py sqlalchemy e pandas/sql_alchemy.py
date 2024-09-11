import sqlite3
import pandas as pd
import sqlalchemy as sqla

engine = sqla.create_engine("sqlite:///28-8 py sqlalchemy e pandas/employees.sqlite")

with engine.connect() as connection:
    with connection.begin():
        connection.execute(sqla.text("""
        create table if not exists employees (
            id integer primary key,
            name varchar(50),
            department varchar(50),
            salary real
        );
        """))
        
        connection.execute(sqla.text("""
            insert into employees (name, department, salary)
            values
                ('Ana', 'HR', 5000),
                ('Paulo', 'IT', 7500),
                ('Carlos', 'Marketing', 6000),
                ('Luis', 'IT', 10000),
                ('Maria', 'HR', 5500);
            """))

df_employees = pd.read_sql('select * from employees', engine)
print(df_employees)
