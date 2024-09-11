from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conectar():
    session = None
    try:
        engine = create_engine("mysql+pymysql://root:root@localhost/infnet", echo=True)
        Session = sessionmaker(bind = engine)
        session = Session()
    except Exception as e:
        print(e)
    return session

def desconetar(session):
    if (session):
        session.close_all()