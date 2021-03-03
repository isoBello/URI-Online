# -*- coding: utf-8 -*-


def solve(N, M, packages):
    for i in range(1, N + 1):
        for j in range(51):
            if packages[i - 1][1] > j:    # O objeto pesa mais que a capacidade da mochila
                M[i][j] = M[i - 1][j]
            else:
                item = M[i - 1][j - packages[i - 1][1]]
                anteriorItem = M[i - 1][j]

                if packages[i - 1][0] + item[1] > anteriorItem[1]:
                    M[i][j][0] = item[0] + packages[i - 1][1]    # Peso
                    M[i][j][1] = item[1] + packages[i - 1][0]   # Valor
                    M[i][j][2] = item[2] - 1                 # Pacotes usados
                else:    # Não houve melhora em colocar o objeto
                    M[i][j] = anteriorItem
    return M[N][50]


if __name__ == "__main__":
    # Solve Santa's Bag
    # Solução baseada no problema da mochila
    casos = int(input())

    while casos > 0:
        pac = int(input())
        packages = [list(map(int, input().split(" "))) for _ in range(pac)]
        M = [[[0, 0, pac] for _ in range(51)] for _ in range(pac + 1)]

        answer = solve(pac, M, packages)
        print("{} brinquedos".format(answer[1]))
        print("Peso: {} kg".format(answer[0]))
        print("sobra(m) {} pacote(s)".format(answer[2]))
        print('')
        casos -= 1
