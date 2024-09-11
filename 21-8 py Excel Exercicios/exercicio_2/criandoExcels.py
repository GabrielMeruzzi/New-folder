import pandas as pd

data1 = {
    'ExpenseID': [1, 2, 3],
    'Category': ['Rent', 'Utilities', 'Groceries'],
    'Amount': [1200, 150, 300]
}

data2 = {
    'ExpenseID': [1, 2, 3],
    'Category': ['Rent', 'Utilities', 'Groceries'],
    'Amount': [500, 1700, 2000]
}

data3 = {
    'ExpenseID': [1, 2, 3],
    'Category': ['Rent', 'Utilities', 'Groceries'],
    'Amount': [200, 50, 5000]
}

data1 = pd.DataFrame(data1)
data1.to_excel('21-8 py Excel Exercicios/exercicio_2/data1.xlsx', index=False)

data2 = pd.DataFrame(data2)
data2.to_excel('21-8 py Excel Exercicios/exercicio_2/data2.xlsx', index=False)

data3 = pd.DataFrame(data3)
data3.to_excel('21-8 py Excel Exercicios/exercicio_2/data3.xlsx', index=False)