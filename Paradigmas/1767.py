# -*- coding: utf-8 -*-


def solve(pac, valor, peso, M, W):
    for i in range(1, pac + 1):
        for j in range(W):
            if not i or not j:
                M[i][j] = 0
            else:
                if peso[i] > j:
                    # O brinquedo não pode ser colocado no saco
                    M[i][j] = M[i - 1][j]
                else:
                    # Analisamos se é melhor colocar ou não colocar o brinquedo no saco, baseado no ganho (max)
                    M[i][j] = max(valor[i] + M[i - 1][j - peso[i]], M[i - 1][j])
    # A resposta ficará em dp[PACKS][W]
    # Agora precisamos analisar a quantidade de pacotes utilizados
    return M[pac + 1][W - 1], count_packs(pac, peso, M, W=51)


def count_packs(pac, peso, M, W=51):
    qtPacks = 0
    qtPeso = 0
    j = W - 1
    for i in range(pac, 1, -1):
        while j > 0:
            if M[i][j] != M[i - 1][j]:
                qtPacks += 1
                qtPeso += peso[i]
                if j - peso[i] >= 0:
                    j -= peso[i]
    return qtPeso, qtPacks


if __name__ == "__main__":
    # Solve Santa's Bag
    # Solução baseada no problema da mochila
    casos = int(input())
    item = 0
    valor = {}
    peso = {}

    while casos > 0:
        pac = int(input())
        for i in range(1, pac + 1):
            qt, w = map(int, input().split(" "))
            valor[i] = qt
            peso[i] = w
            M = [[0] * 51 for _ in range(pac + 2)]  # 51 é o peso limite + 1
        answer, peso, pcts = solve(pac, valor, peso, M, W=51)
        output = "{} brinquedos" + "\n" + "Peso: {} kg" + "\n" + "sobra(m) {} pacote(s)" + "\n"
        print(output.format(answer, peso, pcts))
        casos -= 1
