import pandas as pd
import sqlalchemy as sqla

engine = sqla.create_engine("sqlite:///28-8 py sqlalchemy e pandas/employees.sqlite")

df_employeesIT = pd.read_sql('select * from employees where department like "IT"', engine)
df_employeesAVG = pd.read_sql('select department, avg(salary) from employees group by (department);', engine)

with engine.connect() as connection:
    with connection.begin():
        connection.execute(sqla.text("""
            insert into employees (name, department, salary)
            values
                ('Joao', 'Finance', 8000),
                ('Fernanda', 'Marketing', 7500);
        """))
        
        connection.execute(sqla.text("""
            update employees
            set salary = 9000
            where department = 'IT' and name = 'Paulo'
        """))

df_employees = pd.read_sql('select * from employees', engine)
print(df_employees)