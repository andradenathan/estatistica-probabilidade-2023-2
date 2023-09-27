from random import choice

vitorias = empates = 0

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([s == jogador for s in linha]):
            return True
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def jogada_aleatoria(tabuleiro, jogador):
    vazias = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == " "]
    if vazias:
        linha, coluna = choice(vazias)
        tabuleiro[linha][coluna] = jogador

def jogo_da_velha():
    global vitorias, empates
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = choice(["X", "O"])
    jogo_acabou = False

    while not jogo_acabou:
        jogada_aleatoria(tabuleiro, jogador_atual)
        if verificar_vitoria(tabuleiro, jogador_atual):
            jogo_acabou = True
            vitorias += 1
        elif " " not in [s for linha in tabuleiro for s in linha]:
            empates += 1
            jogo_acabou = True
        jogador_atual = "O" if jogador_atual == "X" else "X"

for i in range(10**6):
  jogo_da_velha()

resultado = (vitorias / (vitorias + empates)) * 100

print(f'{resultado:.2f}%')