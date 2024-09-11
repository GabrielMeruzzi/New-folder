import numpy as np

# Definir um dtype estruturado
dtype_custom = np.dtype([("nome", "U10"), ("idade", "i4"), ("peso", "f4")])

# Criar um array estruturado
pessoas = np.array([("Alice", 25, 55.5), ("Gabriel", 30, 75.2), ("Juan", 35, 68.9)], dtype = dtype_custom )

# Print pelo label
idades = pessoas['idade']

# Selecionar subarrays
primeira_pessoa = pessoas[0]

# Selecionar multiplos elementos
primeiras_duas_pessoas = pessoas[:2]

# Atualizar a idade da primeira pessoa
pessoas[0]["idade"] = 26

# Atualizar o peso dessa pesoas
pessoas["peso"] = [56.0, 76.0, 70.0]

# Ordenação
pessoas_ordenadas = np.sort(pessoas, order = "idade")

# Filtro
pessoas_maior_28 = pessoas[pessoas["idade"] > 28] 



# EXERCICIO


#1
car_data_custom = np.dtype([("nome", "U15"), ("ano", "i4"), ("preco", "f8")])
carros = np.array([("Ferrari", 2024, 100000), 
                   ("Volkwagem", 2000, 67000), 
                   ("Fiat", 1999, 30000), 
                   ("Bugatti", 2025, 1000),
                   ("Linux", 2010, 25000),
                   ("Windows", 2013, 900000)],
                   dtype = car_data_custom)

#2
carros_maior_50 = carros[carros["preco"] > 50.000]

#3
carros[3]["preco"] = 1000000

#4
ordernar_ano = np.sort(carros, order="ano")

#5
# print(carros['nome'])






# EXERCICIO 2

# 1
numeros = np.array([1,2,3,4,5,6,7,8,9,10])

# 2
numeros = np.add(numeros, 5)

# 3
copia = np.copy(numeros)
copia.fill(0)

# 4
max = numeros.max()
min = numeros.min()
soma = numeros.sum()
media = numeros.mean()

# 5
crescente = np.sort(numeros)

rep = np.repeat(numeros, 2)
print(rep)











