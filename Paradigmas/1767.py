# -*- coding: utf-8 -*-


def solve(N, M, packs):
    for i in range(1, N + 1):
        for j in range(51):
            if packs[i - 1][1] > j:    # O objeto pesa mais que a capacidade da mochila
                M[i][j] = M[i - 1][j]
            else:
                object = M[i - 1][j - packs[i - 1][1]]
                anteriorObj = M[i - 1][j]
                gain = packs[i - 1][0] + object[1]
                if gain > anteriorObj[1]:
                    M[i][j][0] = anteriorObj[0] + packs[i - 1][1]   # Peso
                    M[i][j][1] = anteriorObj[1] + packs[i - 1][0]   # Valor
                    M[i][j][2] = anteriorObj[2] - 1                 # Pacotes usados
                else:    # Não houve melhora em colocar o objeto
                    M[i][j] = anteriorObj
    return M[N][50]


if __name__ == "__main__":
    # Solve Santa's Bag
    # Solução baseada no problema da mochila
    casos = int(input())
    valor = {}
    peso = {}

    while casos > 0:
        pac = int(input())
        packages = [list(map(int, input().split(" "))) for _ in range(pac)]
        M = [[[0, 0, pac] for _ in range(51)] for _ in range(pac + 1)]

        answer = solve(pac, M, packages)
        print("{} brinquedos" + "\n" + "Peso: {} kg" + "\n" + "sobra(m) {} pacote(s)".format(answer[0], answer[1],
                                                                                             answer[2]))
        casos -= 1
