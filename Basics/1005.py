# -*- coding: utf-8 -*-

def media(A, B):
    pesos = 3.5 +  7.5
    media = (A + B)/pesos
    print('MEDIA = {0:1.5f}'.format(media))


if __name__ == "__main__":
    A = float(input())
    B = float(input())
    media(A*3.5, B*7.5)