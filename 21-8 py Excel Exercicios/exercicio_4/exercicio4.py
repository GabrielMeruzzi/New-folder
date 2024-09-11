import pandas as pd

df_animais = pd.read_excel('21-8 py Excel Exercicios/exercicio_4/animais.xlsx')

df_vacinas = pd.read_csv('21-8 py Excel Exercicios/exercicio_4/vacinas.csv')

merged = df_animais.merge(df_vacinas)

merged.to_excel('21-8 py Excel Exercicios/exercicio_4/merged.xlsx', index=False)