import numpy as np

""" Array unidimensional """
# print(np.array([1,2,3]))

""" Array bidimensional """
# print(np.array([1,2,3], [4,5,6]))

""" Matriz """
# print(np.matrix([[1,2], [3,4]]))

""" Array de 0 """
# print(np.zero((2,3)))

""" Array de 1 """
# print(np.ones((2,3)))

""" Array com valores randomicos """
# print(np.random.random((2,3)))


""" Operacoes Matematicas """
array = np.array([1,2,3,4])

""" Soma """
# print(array + 10)

""" Concatenar """
array1 = np.array([[1,2], [3,4]])
array2 = np.array([[5,6], [7,8]])

concatenated = np.concatenate((array1, array2), axis = 0)
# print(concatenated)

""" Dividir """
dividir = np.array_split(concatenated,2)
# print(dividir)



""" Estatitica basica """
array = np.array([1,2,3,4,5])
""" Media """
media = np.mean(array)
# print(media)

""" Desvio padrao """
desvPadrao = np.std(media)
# print(desvPadrao)


""" Indexacao e Slicing """
array = np.array([1,2,3,4,5])
""" Acessar o primeiro elemento """
# print(array[0])
""" Slicing """
# print(array[1:4])






""" EXERCICIOS """

# 1
array = np.zeros([10])
array[5] = 1
print(array)

# 2
array = np.array(([0,8,0], [8,0,8], [0,8,0]))

# 3
array1 = np.array([1,2,3])
array2 = np.array([2,3,4])

soma = array1 + array2
print(soma)

# 4
a = np.array([10,15,25,30,35])
b = a[1:4]
print(b)

# 5
random = np.random.random((5,5))
max = random.max()
min = random.min()

# 6
random2 = np.random.randint(1, 51, size=(6,6))
print(random2)

# 7
b = np.array([1,2,3,4,5,6,7,8,9,10])
print(b.reshape(2,5))











