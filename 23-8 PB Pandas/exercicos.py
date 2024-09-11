import pandas as pd

# 1
serie = pd.Series([2, 4, 6, 8, 10])
# print(serie)


# 2
data = {
    'Produto': ['Sabonete', 'Shampoo', 'Condicionador', 'Skin Care'],
    'Quantidade': [10, 21, 15, 25],
    'Preço': [10.99, 21.99, 15.99, 25.99]
}

df = pd.DataFrame(data)
# print(df)


# 3
# 3_linha = df.loc[2])


# 4
df.insert(3, 'Total', df['Quantidade'] * df['Preço'])


# 5
df.sort_values(by='Total', ascending=False)
# print(df)


# 6
df.loc[df['Quantidade'] > 20] = 25
# print(df)


# 7
data2 = {
    'Valores': [1, None, 3, None, 5, 6, None, None]
}

df2 = pd.DataFrame(data2)


# 8

data3 = {
    'Teste': [1, 2, 3, 4, 5]
} 
data4 = {
    'Teste': [6, 7, 8, 9, 10]
} 

