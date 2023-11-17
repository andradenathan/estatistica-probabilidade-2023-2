import numpy as np

SUPERIOR_ESQ = (0,0)
INFERIOR_DIR = (4,4)

VALORES_PERMITIDOS_TBL = [0, 1, 2, 3, 4]

def criar_tabuleiro():
  return np.array([
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
  ])

def definir_posicoes():
  linha = int(input('Escolha a linha da posição (de 0 à 4): '))
  coluna = int(input('Escolha a coluna da posição (de 0 à 4): '))
  if coluna not in VALORES_PERMITIDOS_TBL or linha not in VALORES_PERMITIDOS_TBL:
    raise ValueError('Você inseriu uma posição no tabuleiro que não existe. Por favor, execute o programa novamente e escolha de 0 à 4.')
  return linha, coluna

def alterar_posicao_tabuleiro(pos, caminho, tabuleiro):
  tabuleiro[pos] += 1
  caminho.append(pos)
  return tabuleiro, caminho

def pegar_posicao_permitida(movimentos):
  # preciso ter a quantidade de movimentos permitidos para
  # dar uma probabilidade uniforme para cada pos. adjacente à pos. atual
  qtd_movimentos = len(movimentos)
  indices_movimentos_permitidos = [i for i in range(qtd_movimentos)]
  probabilidade = [1/qtd_movimentos] * qtd_movimentos
  return np.random.choice(indices_movimentos_permitidos, p=probabilidade)

def checar_movimento_dada_posicao(posicao_atual):
  linha, coluna = posicao_atual
  tamanho_tabuleiro = 5
  movimentos_permitidos = [
      (linha + 1, coluna) if linha + 1 < tamanho_tabuleiro else None,
      (linha - 1, coluna) if linha - 1 >= 0 else None,
      (linha, coluna + 1) if coluna + 1 < tamanho_tabuleiro else None,
      (linha, coluna - 1) if coluna - 1 >= 0 else None
  ]
  movimentos = [movimento for movimento in movimentos_permitidos if movimento is not None]
  return movimentos[pegar_posicao_permitida(movimentos)]


def mover(posicao_inicio, caminho, tabuleiro):
  pos = posicao_inicio
  while pos != SUPERIOR_ESQ and pos != INFERIOR_DIR:
    (tabuleiro_atualizado, caminho_atualizado) = alterar_posicao_tabuleiro(pos, caminho, tabuleiro)
    pos = checar_movimento_dada_posicao(pos)
  
  if pos == SUPERIOR_ESQ:
    # superior esquerdo é uma trap
    return tabuleiro_atualizado, SUPERIOR_ESQ

  # inferior direito é uma trap
  return tabuleiro_atualizado, INFERIOR_DIR  