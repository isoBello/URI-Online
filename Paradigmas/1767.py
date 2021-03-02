# -*- coding: utf-8 -*-
W = 51
PACKS = 101


class Bag:
    def __init__(self, toy, w):
        self.toy = toy
        self.peso = w




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
            saco[i].append(Bag(qt, peso))
        # solve(saco, M)
        casos -= 1
