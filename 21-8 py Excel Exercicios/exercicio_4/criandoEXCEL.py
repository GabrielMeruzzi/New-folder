import pandas as pd

data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['Rex', 'Garfield', 'Nemo', 'Tweety', 'Spike'],
    'Espécie': ['Cachorro', 'Gato', 'Peixe', 'Pássaro', 'Cachorro']
}

data_csv = {
    'ID': [1, 2, 3, 4, 5],
    'Consultas': [3, 2, 1, 0, 4],
    'Vacinas': ['Sim', 'Não', 'Sim', 'Não', 'Sim']
}

data_csv = pd.DataFrame(data_csv)
data_csv.to_csv('21-8 py Excel Exercicios/exercicio_4/vacinas.csv', index=False)


data1 = pd.DataFrame(data1)
data1.to_excel('21-8 py Excel Exercicios/exercicio_4/animais.xlsx', index=False)
