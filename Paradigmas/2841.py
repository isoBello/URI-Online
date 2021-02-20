# -*- coding: utf-8 -*-


# Solving Dabriel e Sua Festa
def solve(tree, people):
    length = people + 2
    dp = [[-1] * 4 for _ in range(length)]

    for i in range(length - 1):
        for j in range(3):
            if i == 0:
                dp[i][j] = 0
            elif i > 0 and j == 0:
                child = tree[i][1]
                fun_relates = 0
                for c in child:
                    fun_relates += tree[c][0]
                dp[i][j] = fun_relates
            elif i > 0 and j == 1:
                child = tree[i][1]
                fun_relates = 0
                for c in child:
                    for g in tree[c][1]:
                        fun_relates += tree[g][0]
                dp[i][j] = fun_relates + tree[i][0]
            else:
                dp[i][j] = max(dp[i][0], dp[i][1])
                dp[length-1][i] = dp[i][j]
    return max(dp[length-1])


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

    size = max(set(chefes))
    chefes.insert(0, 0)
    C = subordinados(chefes, fun)

    print(solve(C, size))
