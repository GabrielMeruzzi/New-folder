import pandas as pd

df = pd.read_excel('21-8 py Excel Exercicios/exercicio.xlsx')

pd.to_datetime(df['date'])

temper_filter = df.groupby('city')['temperature'].mean()

temper_filter.to_excel('21-8 py Excel Exercicios/temperaturaFiltrada.xlsx')

















