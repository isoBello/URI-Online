# -*- coding: utf-8 -*-
from collections import defaultdict


# Solving Dabriel e Sua Festa
class Tree:
    def __init__(self, n, party):
        self.nodes = set(range(1, n + 1))
        self.hierarchy = defaultdict(list)
        self.animation = party
        self.animation.insert(0, 0)

    def addConnection(self, u, v):
        self.hierarchy[u].append(v)
        self.hierarchy[v].append(u)


def solve(node, parent, M, t):
    invite = 0
    exclude = 0

    for child in t.hierarchy[node]:
        if child == parent:
            continue

        solve(child, node, M, t)

        # Inclui o n-th nó e não inclui seus filhos
        invite += M[child][1]

        # Não inclui o n-th nó, então inclui seus filhos ou não
        exclude += max(M[child][0], M[child][1])
    M[node][0] = t.animation[node] + invite
    M[node][1] = exclude


if __name__ == "__main__":
    pessoas = int(input())
    fun = list(map(int, input().split(" ")))
    chefes = list(map(int, input().split(" ")))

    tree = Tree(pessoas, fun)
    for i in range(len(chefes)):     # Constroi a árvore
        chefe = chefes[i]
        subordinado = i + 2
        tree.addConnection(chefe, subordinado)

    # M é a matriz de programação dinâmica
    # M[i][0] indica que a pessoa i foi convidada
    # M[i][1] indica que a pessoa i não foi convidada
    # [pessoas + 1][3] é só para não dar erro de acesso
    M = [[0] * 3 for _ in range(pessoas + 1)]

    # Faz uma busca transversal na árvore. Importante porque queremos ir das folhas à raiz.
    # Porque?
    # Porque a relação de recorrência é:
    # max { i foi convidado + os subordinados de seus subordinados
    #     { i não foi convidado + seus subordinados foram
    # Para saber o valor dos subordinados de seus subordinados, é preciso que eles já tenham sido calculados, e isso vem
    # da busca transversal
    # A primeira tentativa é com o DFS recursivo.
    # Não consegui fazer o DFS iterativo porque ficava preso nas folhas. Tentando consertar time limit simplificando
    # a construção da árvore.
    solve(1, 1, M, tree)
    print(max(M[1][0], M[1][1]))
