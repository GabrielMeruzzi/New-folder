import pandas as pd

data = {
    'date': ['2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03', '2024-07-03'],
    'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'temperature': [26, 31, 20, 15, 3, 7]
}

df = pd.DataFrame(data)
with pd.ExcelWriter('21-8 py Excel Exercicios/exercicio.xlsx') as writer:
    df.to_excel(writer, sheet_name='data', index=False)