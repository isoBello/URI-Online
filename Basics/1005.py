# -*- coding: utf-8 -*-

def media(notas):
    try:
        media = (notas[0] + notas[1])/(notas[2] + notas[3])
        print('MEDIA = {0:1.5f}'.format(media))
    except expression as identifier:
        pass

if __name__ == "__main__":
    A = float(input())
    B = float(input())
    notas = [A*3.5, B*7.5, 3.5, 7.5]
    media(notas)