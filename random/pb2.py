""" 1 """
dados_alunos = {
    'nome': 'kaka',
    'idade': 40,
    'curso': 'futebolistico'
}
print('CURSO:', dados_alunos['curso'])


""" 2 """
dados_alunos['nota'] = 10
dados_alunos['idade'] = 41


""" 3 """
removido = dados_alunos.pop('curso')
print('POP', removido)
print(dados_alunos)


""" 4 """
for chave, valor in dados_alunos.items():
    print(chave, valor)


""" 5 """
texto = "o o rato roeu a roupa do rei de roma"
palavras = texto.split()
newDict = {}
for p in palavras:
        if p in newDict:
            newDict[p] += 1
        else:
            newDict[p] = 1
print(newDict)


""" 6 """
produtos = {
    "p1": 10,
    "p2": 20,
    "p3": 15
}
newLista = {}
for chave, valor in produtos.items():
    if valor > 15:
        newLista[chave] = valor
print(newLista)


""" 7 """
produto = {
    'produto': 'rexona nao te abandona',
    'seg': 20,
    'ter': 30 
}

total_vendas_em_uma_semana = produto['seg'] + produto['ter']
print(produto)
print(total_vendas_em_uma_semana)


