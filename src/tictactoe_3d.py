from random import choice

vitorias_3d = empates_3d = 0

def criar_tabuleiro_3d(dimensao):
    tabuleiro = []
    for _ in range(dimensao):
        camada = []
        for _ in range(dimensao):
            linha = []
            for _ in range(dimensao):
                linha.append(" ")
            camada.append(linha)
        tabuleiro.append(camada)
    return tabuleiro

def verificar_vitoria(tabuleiro, jogador):
    dimensao = len(tabuleiro)

    for camada in tabuleiro:
        for linha in camada:
            if all([s == jogador for s in linha]):
                return True

    for coluna in range(dimensao):
        for camada in range(dimensao):
            if all([tabuleiro[camada][linha][coluna] == jogador for linha in range(dimensao)]):
                return True

    for camada in range(dimensao):
        if all([tabuleiro[camada][i][i] == jogador for i in range(dimensao)]) or all([tabuleiro[camada][i][dimensao - 1 - i] == jogador for i in range(dimensao)]):
            return True

    for dim in range(dimensao):
        for coluna in range(dimensao):
            if all([tabuleiro[camada][dim][coluna] == jogador for camada in range(dimensao)]):
                return True

    if all([tabuleiro[i][i][i] == jogador for i in range(dimensao)]) or all([tabuleiro[i][i][dimensao - 1 - i] == jogador for i in range(dimensao)]):
        return True

    return False

def jogada_aleatoria_3d(tabuleiro, jogador):
    dimensao = len(tabuleiro)
    vazias = []
    for camada in range(dimensao):
        for linha in range(dimensao):
            for coluna in range(dimensao):
                if tabuleiro[camada][linha][coluna] == " ":
                    vazias.append((camada, linha, coluna))
    if vazias:
        camada, linha, coluna = choice(vazias)
        tabuleiro[camada][linha][coluna] = jogador

def jogo_da_velha_3d(dimensao):
    global vitorias_3d, empates_3d
    tabuleiro = criar_tabuleiro_3d(dimensao)
    jogador_atual = choice(["X", "O"])
    jogo_acabou = False

    while not jogo_acabou:
        jogada_aleatoria_3d(tabuleiro, jogador_atual)
        if verificar_vitoria(tabuleiro, jogador_atual):
            vitorias_3d += 1
            jogo_acabou = True
        elif " " not in [s for camada in tabuleiro for linha in camada for s in linha]:
            empates_3d += 1
            jogo_acabou = True
        jogador_atual = "O" if jogador_atual == "X" else "X"

for i in range(10**6):
  jogo_da_velha_3d(3)

resultado_3d = (vitorias_3d / (vitorias_3d + empates_3d)) * 100
f'{resultado_3d:.2f}%', vitorias_3d, empates_3d