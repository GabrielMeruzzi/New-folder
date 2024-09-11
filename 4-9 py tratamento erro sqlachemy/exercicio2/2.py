x = [['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', 'X', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_']]

def posicaoX():
    for linha_index, linha in enumerate(x):
        for coluna_index, valor in enumerate(linha):
            if valor == 'X':
                return (linha_index, coluna_index)

posicaoAtual = posicaoX()
def moverPosicaoEscolhida(x, y):
    if abs(x - posicaoAtual[0]) and abs(y - posicaoAtual[1]):
        print('Foi')
posicaoX()

moverPosicaoEscolhida(0, 2)