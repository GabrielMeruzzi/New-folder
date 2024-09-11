import pandas as pd
import glob


combinedGlob = glob.glob('21-8 py Excel Exercicios/exercicio_2/data*.xlsx')

all_ex = pd.DataFrame()

for df in combinedGlob:
    w = pd.read_excel(df)
    all_ex = pd.concat([all_ex, w], ignore_index=True)

expensive = all_ex.groupby('Category')['Amount'].sum().reset_index()

expensive.to_excel('21-8 py Excel Exercicios/exercicio_2/gastos.xlsx')








