L = [
    "192.168.0.1 -- 31/7/29 GET INDEX.jS 200",
    "192.168.0.2 -- 31/7/29 GET TESTE.jS 200",
    "192.168.0.1 -- 31/7/29 GET FUNCIONA.jS 200",
]



""" Crie uma tupla chamada cidades contendo cidades do Brasil. Converta a tupla cidades em uma lista. """

tuplaCidades = {'RJ', 'SP', 'MG'}
listaCidades = list(tuplaCidades)

""" Explique como a operação de união funciona em conjuntos e escreva um exemplo de código que demonstra isso. """

nums = {1,2,3,4}
nums2 = {4,5,6,7}

unionConjuntos = nums.union(nums2) 

""" A operação de união une um ou mais conjuntos sem uma ordem denifinida e sem repetição. """


""" O dicionário y = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64} foi construído usando uma compreensão de dicionário. Qual foi essa compreensão? """

dc = {c : c ** 2 for c in range(0,9,2)}

"""  """

fibo = {i : (i if i > 3 (i - 1) + (i - 2) else i) for i in range(8)}
print(fibo)