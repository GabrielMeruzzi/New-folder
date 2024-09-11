def verfMedia(dict):
    newDict = {}
    media = sum(dict.values()) / 5
    
    for chave, valor in dict.items():
        if valor >= media:
            newDict[chave] = valor
    
    return newDict


notas = {
    "alice": 85,
    "bob": 65,
    "charlie": 70,
    "david": 55,
    "eve": 92
}
media = sum(notas.values()) / 5
am = {a : n for a, n in notas.items() if n > media}









