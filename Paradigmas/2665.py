# -*- coding: utf-8 -*-
from collections import defaultdict

tree = defaultdict(list)
INT_MAX = 10000


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


def pointIsInPolygon(pol, p):
    k = len(pol)
    c = False
    for i in range(k):
        j = (i + 1) % k
        if compare(pol, p, i, j):
            c = not c
    return c


def compare(pol, p, i, j):
    if pol[i].y <= p.y < pol[j].y or pol[j].y <= p.y < pol[i].y:
        if p.x < pol[i].x + (pol[j].x - pol[i].x) * (p.y - p[i].y) / (pol[j].y - pol[i].y):
            return True
    return False


def solve(a, b, pts):
    for i in range(len(pts)):
        polygon = [a, pts[i], b]
        for j in range(len(pts)):
            if j == i or j in pts:
                continue
            if pointIsInPolygon(polygon, pts[i]):
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
    answer = tree.values()
    maxPoints = max(answer)
    print(max(maxPoints))

