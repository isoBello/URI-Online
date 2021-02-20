# -*- coding: utf-8 -*-


# Solving Dabriel e Sua Festa
def solve(node, parent, dp, animation, t):
    sum1 = 0
    sum2 = 0

    for child in t[node]:
        if child == parent:
            continue

        solve(child, node, dp, animation, t)

        # Inclui o n-th nó e não inclui seus filhos
        sum1 += dp[child][1]

        # Não inclui o nó, então inclui seus filhos ou não
        sum2 += max(dp[child][0], dp[child][1])
    dp[node][0] = profit[node] + sum1
    dp[node][1] = sum2


if __name__ == "__main__":
    pessoas = int(input())
    fun = list(map(int, input().split(" ")))
    chefes = list(map(int, input().split(" ")))

    k = pessoas + 1
    tree = [[] for i in range(k)]

    # Dummys
    chefes.insert(0, 0)
    chefes.insert(1, 0)
    fun.insert(0, 0)

    for i in range(1, k):
        try:
            subordinados = chefes[i]
            subordinados = [subordinados]
        except ValueError:
            continue

        if i in chefes:
            p = [j for j, x in enumerate(chefes) if x == i]
            subordinados = subordinados + p
        tree[i] = subordinados

    profit = [0 for i in range(k)]
    for i in range(1, k):
        profit[i] = fun[i]

    dp = [[0] * 3 for _ in range(k)]
    tree[1].remove(0)

    solve(1, 1, dp, profit, tree)
    print(max(dp[1][0], dp[1][1]))
