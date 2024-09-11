import pandas as pd

data1 = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Nome': ['João', 'Maria', 'Carlos', 'Jessica', 'Luis', 'Ana', 'Pedro', 'Pablo'],
    'Idade': [25, 28, 24, 41, 38, 21, 19, 40],
    'Departamento': ['TI', 'R.H', 'EC', 'TI', 'TI', 'EC', 'EC', 'R.H'],
    'Salário': ['', 6000, 5000, 9000, 12000, 7000, '', 8000]
}

""" data2 = {
    'ID': [2, 3, 4],
    'Cidade': ['Rio de Janeiro', 'Belo Horizonte', 'São Paulo'],
    'Salário': [2500, 2700, 3000]
} """

df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

with pd.ExcelWriter('file1.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Pessoa', index=False)
    print('Arquivo criado com sucesso!')
