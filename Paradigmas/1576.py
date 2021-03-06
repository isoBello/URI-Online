# -*- coding: utf-8 -*-

def solve(E):
    for j in range(len(E.keys())):




if __name__ == "__main__":
    i = 0
    edificios = {}

    while True:
        try:
            L, H, R = map(int, input().split(" "))
            edificios[i].append((L, H, R))
            i += 1
        except EOFError:
            break

    # Segundo o livro do Manber, a estratégia para resolver este problema é parecida com o MergeSort.
    # Para cada edifício, armazenar L com um valor negativo de H e R com H real
    print(solve(edificios))
