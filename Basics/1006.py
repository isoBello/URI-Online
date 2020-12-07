# -*- coding: utf-8 -*-

def media(notas):
    try:
        soma = 0
        pesos = 0
        for i in range(0, 3):
            soma += notas[i]
        for i in range(3, len(notas)):
            pesos += notas[i]
        print('MEDIA = {0:1.1f}'.format(soma/pesos))
    except expression as identifier:
        pass

if __name__ == "__main__":
    A = float(input())
    B = float(input())
    C = float(input())
    notas = [A*2, B*3, C*5, 2, 3, 5]
    media(notas)