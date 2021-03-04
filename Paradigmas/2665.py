# -*- coding: utf-8 -*-
from collections import defaultdict

tree = defaultdict(list)
INT_MAX = 10000


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


def solve(a, b, pts):
    for i in range(len(pts)):
        polygon = [a, pts[i], b]
        for j in range(len(pts)):
            if pts[j] in polygon:
                continue
            if PointIsInPolygon(polygon, pts[j]):
                tree[i].append(j)




if __name__ == "__main__":
    P, Xa, Xb = map(int, input().split(" "))
    points = []

    # Ancoras
    A = Point(Xa, 0)
    B = Point(Xb, 0)

    for point in range(P):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))

    # Segunda abordagem: Determinar se o ponto está no polígono (a maioria são triângulos?) possivelmente não convexo.
    # Retorna True para pontos estritamente externos, e False para pontos restantes.
    solve(A, B, points)


