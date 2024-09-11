import pandas as pd

df = pd.read_excel('file1.xlsx', sheet_name='data')

salarios = df['Salário']


df['SalarioMaiorQ8000'] = df['Salário'] >= 8000

with pd.ExcelWriter('file2.xlsx') as writer:
    df.to_excel(writer, sheet_name='data', index=False)




