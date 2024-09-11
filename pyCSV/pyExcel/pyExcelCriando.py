import pandas as pd

data1 = {
    'ID': [1, 2, 3],
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Cargo': ['Analista', 'Dev', 'Gerente']
}

data2 = {
    'ID': [1, 2, 3],
    'Avaliação': ['Excelente', 'Bom', 'Regular']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Pessoas', index=False)
    print('Arquivo criado com sucesso!')
    
    
    
    # Junto com colunas
""" with pd.ExcelWriter('file3.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Pessoas', index=False)
    df2.to_excel(writer, sheet_name='Avaliações', index=False)
    print('Arquivo criado com sucesso!') """

