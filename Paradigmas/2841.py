# -*- coding: utf-8 -*-
from collections import defaultdict


# Solving Dabriel e Sua Festa
def fun_party(tree):
    animation = []
    grandchild = []

    for k, node in tree.items():
        if not node[1]:
            pass
        else:
            for no in node[1]:
                if tree[no][1]:
                    for n in tree[no][1]:
                        grandchild.append((n, tree[n][0]))
        grands_fun = grands(grandchild)
        childs_fun = childs(tree, k)
        animation.append(max(tree[k][0] + grands_fun, childs_fun))

    return animation[0]


def grands(vo):
    sum_fun = 0
    for neto in vo:
        sum_fun += neto[1]
    return sum_fun


def childs(tree, k):
    sum_fun = 0
    for node in tree[k][1]:
        sum_fun += tree[node][0]
    return sum_fun


def subordinados(boss, profits):
    organization = {}
    node = 1

    for profit in profits:
        if node in boss:
            indices = [i+1 for i, x in enumerate(boss) if x == node]
            infos = [profit, indices]
        else:
            infos = [profit, []]
        organization[node] = infos
        node += 1
    return organization


if __name__ == "__main__":
    pessoas = int(input())
    fun = list(map(int, input().split(" ")))
    chefes = list(map(int, input().split(" ")))

    chefes.insert(0, 0)

    C = subordinados(chefes, fun)
    print(fun_party(C))
