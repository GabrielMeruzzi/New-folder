import pandas as pd

file1 = pd.ExcelFile('file1.xlsx')
file2 = pd.ExcelFile('file2.xlsx')

print('Planilhas disp:', file1.sheet_names)
print('Planilhas disp:', file2.sheet_names)