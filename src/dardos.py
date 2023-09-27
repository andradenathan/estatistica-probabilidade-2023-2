from random import random
from math import pi, sqrt

acertou = errou = 0
RAIO = 1

for _ in range(10**6):
    x, y = (random(), random())
    distancia = sqrt((x-1) ** 2 + (y-1) ** 2)
    if distancia < RAIO:
        acertou += 1
    else:
        errou += 1

n = acertou+errou
total = acertou/n
erro = abs(total-pi/4)