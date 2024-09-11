from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"
    
    id_aluno = Column(Integer, primary_key=True)
    nome_aluno = Column(String)
    
    def __init__(self, nome):
        self.nome_aluno = nome
    
    def __str__(self):
        return f"{self.id_aluno}: {self.nome_aluno}"