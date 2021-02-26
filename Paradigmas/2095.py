# -*- coding: utf-8 -*-
# esquerda é global para que a busca não comece do 0 toda vez, escolhendo os mesmos elementos
esquerda = 0


def binarySearch(j, Q):
    global esquerda
    direita = len(Q) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if j <= Q[meio]:  # Se meu elemento é menor ou igual, perdi a batalha, analiso o próximo
            direita = meio - 1
        else:    # Achei alguém menor que eu, ganhei esta batalha, não preciso continuar procurando
            esquerda += 1
            return 1
    return 0


# Solve War
if __name__ == "__main__":
    soldados = int(input())
    quadradonianos = list(map(int, input().split(" ")))
    noglonianos = list(map(int, input().split(" ")))

    quadradonianos.sort()
    noglonianos.sort()

    R = 0
    # ------------Tentativa com busca binária, ordenando o segundo vetor--------------
    # Não deu certo a busca. Tentando colocar esquerda como global
    # A ideia veio porque o segundo teste sempre dava resposta = 4
    # Percebi que eu nunca ''excluía'' um soldado, a busca sempre começava de 0
    for i in range(0, soldados):
        isMenor = binarySearch(noglonianos[i], quadradonianos)
        if isMenor == 1:   # Achei alguém menor que eu, ganhei uma batalha
            R += 1
    print(R)
