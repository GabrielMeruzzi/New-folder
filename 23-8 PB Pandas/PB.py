import pandas as pd

nomes = ['Ana', 'Bruno', 'Carla']
idades = [21, 20, 22]
dados = list(zip(nomes, idades))
print(dados)

df = pd.DataFrame(data = dados)
print(df)