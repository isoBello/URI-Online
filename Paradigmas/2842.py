# -*- coding: utf-8 -*-

# Solving Dabriel e Suas Strings
def concatenar(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b and b in a:
        return size_a
    elif size_b > size_a and a in b:
        return size_b
    else:
        k = size_a + 2
        n = size_b + 2
        dinamic = [[0] * n for _ in range(k)]

        for i in range(k - 1):
            for j in range(n - 1):
                if not i:
                    dinamic[i][j] = j
                elif not j:
                    dinamic[i][j] = i
                elif a[i - 1] == b[j - 1]:
                    dinamic[i][j] = 1 + dinamic[i - 1][j - 1]
                else:
                    dinamic[i][j] = 1 + min(dinamic[i - 1][j], dinamic[i][j - 1])
        return dinamic[size_a][size_b]


if __name__ == "__main__":
    A = input()
    B = input()

    print(concatenar(A, B))
