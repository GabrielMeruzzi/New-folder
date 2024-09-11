import sqlite3
import pandas as pd
import sqlalchemy as sqla

con = sqlite3.connect('28-8 py sqlalchemy e pandas/mydata.db')

query = """
CREATE TABLE IF NOT EXISTS test (
    a varchar(20),
    b varchar(20),
    c real,
    d interger
    );
"""

con.execute(query)
con.commit()

data = [("Atlanta", "Georgia", 1.25, 6),
        ("Tallahassee", "Florida", 2.6, 3),
        ("Sacramento", "California", 1.7, 5)]

stmt = 'insert into test values (?, ?, ?, ?)'
con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
print(df)

con.close()




