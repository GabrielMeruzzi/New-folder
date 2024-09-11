import pandas as pd

df = pd.read_excel('21-8 py Excel Exercicios/exercicio_3/data1.xlsx')

avg = df.groupby('Estudante').agg({'Nota': 'mean'}).reset_index()

dataAVG = {}

for i in avg:
    dataAVG['Estudante'] = i['Nota']

print(dataAVG)