# -*- coding: utf-8 -*-


# Solving Dabriel e Sua Festa
def solve(tree):
    size = len(tree) + 1
    dp = [[0] * size for _ in range(size)]
    for i in range(1, size - 1):
        k = 0
        for j in range(1, size - 1):
            if not tree[i][1] and i == j:
                dp[i][j] = tree[i][0]
            elif tree[i][1] and i == j:
                dp[i][j] = tree[i][0]
            elif tree[i][1] and j in tree[i][1]:
                try:
                    while k < len(tree[j][1]):
                        no = tree[j][1][k]
                        dp[i][j] = max(tree[i][0] + tree[no][0], tree[j][0])
                        k += 1
                except IndexError:
                    dp[i][j] = max(tree[i][0] + 0, tree[j][0])
    return dp


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

    print(solve(C))
