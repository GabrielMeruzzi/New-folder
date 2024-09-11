import pandas as pd

xlsx = pd.ExcelFile('output.xlsx')

print('Planilhas disp:', xlsx.sheet_names)

df_pessoas = xlsx.parse('Pessoas')
print('\nDados da planilha Pessoas:')
print(df_pessoas)

df_produtos = xlsx.parse('Produtos')
print('\nDados da planilha Produtos:')
print(df_produtos)