# -*- coding: utf-8 -*-


def solve(dp, packs):
    for i in range(1, len(dp)):
        for j in range(51):
            if packs[i - 1][1] > j:    # O objeto pesa mais que a capacidade da mochila



if __name__ == "__main__":
    # Solve Santa's Bag
    # Solução baseada no problema da mochila
    casos = int(input())
    valor = {}
    peso = {}

    while casos > 0:
        pac = int(input())
        packages = [map(int, input.split(" ")) for _ in range(pac)]
        M = [[[0, 0, pac] for _ in range(51)] for _ in range(pac + 1)]

        solve(M, packages)
        casos -= 1
