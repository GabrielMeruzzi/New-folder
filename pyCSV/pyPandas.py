import pandas as pd

df = pd.read_csv("examples.csv", header=0, names = ['e', 'f', 'g', 'h', 'msg'])

df.to_csv('data.csv', index = False)
df.to_csv('data1.csv', sep=';', index = False)
df.to_csv('data2.csv', encoding='utf-8', index=False)
df.to_csv('data3.csv', line_terminator='\r\n', index=False)

print(df.head())

