# -*- coding: utf-8 -*-


# Solving Dabriel e Sua Festa
def dfs(node, parent, d1, d2, profit, t):
    sum1 = 0
    sum2 = 0
    for child in t[node]:
        if child == parent:
            continue
        dfs(child, node, d1, d2, profit, t)

        # Inclui o n-th nó e não inclui seus filhos
        sum1 += d2[child]

        # Não inclui o nó, então inclui seus filhos ou não
        sum2 == max(d1[child], d2[child])
    d1[node] = profit[node] + sum1
    d1[node] = sum2


if __name__ == "__main__":
    pessoas = int(input())
    fun = list(map(int, input().split(" ")))
    chefes = list(map(int, input().split(" ")))
    tree = {}

    # Dummys
    chefes.insert(0, -1)
    chefes.insert(0, -1)

    fun.insert(0, -1)
    fun.insert(pessoas+1, -1)

    for i in range(1, pessoas + 1):
        if i in chefes:
            subordinados = [j for j, x in enumerate(chefes) if x == i]
            try:
                subordinados.append(chefes[i])
            except ValueError:
                continue
        else:
            subordinados = chefes[i]
            subordinados = [subordinados]
        tree[i] = subordinados

    dp1 = [0 for i in range(pessoas + 2)]
    dp2 = [0 for i in range(pessoas + 2)]

    tree[1].remove(-1)
    dfs(1, 1, dp1, dp2, fun, tree)
    print(max(dp1[1], dp2[1]))
