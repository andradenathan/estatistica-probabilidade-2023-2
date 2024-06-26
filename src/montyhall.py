from random import random, choice, randrange, randint
from math import pi, sqrt

vitorias_ficar = vitorias_mudar = 0

for _ in range(10**6):
    portas = [0, 0, 1]
    porta_escolhida = randint(0, 2)
    portas_restantes = []
    for porta in range(3):
        if porta != porta_escolhida and portas[porta] == 0:
            portas_restantes.append(porta)
    porta_aberta = choice(portas_restantes)
    escolha_mudar = [i for i in range(3) if i != porta_escolhida and i != porta_aberta][0]

    if portas[porta_escolhida] == 1:
        vitorias_ficar += 1

    if portas[escolha_mudar] == 1:
        vitorias_mudar += 1

probabilidade_ficar = (vitorias_ficar / (vitorias_ficar + vitorias_mudar)) * 100
probabilidade_mudar = (vitorias_mudar / (vitorias_ficar + vitorias_mudar)) * 100

print(f'Probabilidade de ganhar se a porta não mudar: {probabilidade_ficar:.2f}%')
print(f'Probabilidade de ganhar se a porta mudar: {probabilidade_mudar:.2f}%')
