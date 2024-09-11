import pandas as pd

data1 = {
    'Estudante': ['Ana', 'Ana', 'Pablo', 'Pablo', 'Maria', 'Maria'],
    'Disciplina': ['Mat', 'Hist', 'Mat', 'Hist', 'Mat', 'Hist'],
    'Nota': [9, 8.5, 8, 6.5, 10, 10]
}


data1 = pd.DataFrame(data1)
data1.to_excel('21-8 py Excel Exercicios/exercicio_3/data1.xlsx', index=False)
