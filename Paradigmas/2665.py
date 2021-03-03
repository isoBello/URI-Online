# -*- coding: utf-8 -*-
from functools import reduce

tree = {}


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


def determinante(a, b, c):
    matriz = [[a.x, a.y], [b.x, b.y], [c.x, c.y]]
    order = len(matriz)
    posdet = 0
    for i in range(order):
        posdet += reduce((lambda x, y: x * y), [matriz[(i+j) % order][j] for j in range(order)])
    negdet = 0
    for i in range(order):
        negdet += reduce((lambda x, y: x * y), [matriz[(order-i-j) % order][j] for j in range(order)])
    return posdet-negdet


def solve(a, b, pts):
    distances = []
    for i in range(pts):
        D = determinante(A, B, pts[i])




if __name__ == "__main__":
    P, Xa, Xb = map(int, input().split(" "))
    points = []

    # Ancoras
    A = Point(Xa, 0)
    B = Point(Xb, 0)

    for point in range(P):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))


    solve(A, B, points)
