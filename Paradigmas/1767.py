# -*- coding: utf-8 -*-
from collections import defaultdict
W = 51
PACKS = 101


class Bag:
    def __init__(self, toy, w):
        self.toy = toy
        self.peso = w


def solve(P, packages, dp):
    global PACKS, W
    for i in range(P):
        for j in range(W):
            if not i or not j:
                dp[i][j] = 0
            else:
                if packages[i].peso > j:
                    # O brinquedo não pode ser colocado no saco
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Analisamos se é melhor colocar ou não colocar o brinquedo no saco, baseado no ganho (max)
                    dp[i][j] = max(packages[i].toy + dp[i - 1][j - packages[i].peso], dp[i - 1][j])
    # A resposta ficará em dp[PACKS][W]
    # Agora precisamos analisar a quantidade de pacotes utilizados
    return dp[PACKS][W], count_packs(P, dp, packages)


def count_packs(P, dp, packs):
    qtPacks = 0
    qtPeso = 0
    for i in range(P, 0, -1):
        for j in range(W, 0, -1):
            if dp[i][j] != dp[i - 1][j]:
                qtPacks += 1
                qtPeso += packs[i].peso
                if j - packs[i].peso >= 0:
                    j -= packs[i].peso
    return qtPeso, qtPacks


if __name__ == "__main__":
    # Solve Santa's Bag
    # Solução baseada no problema da mochila
    casos = int(input())
    item = 0
    saco = {k: Bag(0, 0) for k in range(0, PACKS)}  # 101 é a qtd de pacotes + 1
    M = [[0] * PACKS for _ in range(W)]  # 51 é o peso limite + 1

    while casos > 0:
        pac = int(input())
        for i in range(1, pac + 1):
            qt, peso = map(int, input().split(" "))
            saco[i] = Bag(qt, peso)
        answer, peso, pcts = solve(pac, saco, M)
        output = "{} brinquedos" + "\n" + "Peso: {} kg" + "\n" + "sobra(m) {} pacote(s)" + "\n"
        print(output.format(answer, peso, pcts))
        casos -= 1
