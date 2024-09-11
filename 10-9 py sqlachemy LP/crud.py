from conectar_bd import *
from models import *

def consultar_todos():
    session = conectar()
    try:
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            print(aluno)
    except Exception as e:
        print(e)
    finally:
        desconetar(session)