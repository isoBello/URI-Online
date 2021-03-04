# -*- coding: utf-8 -*-
from collections import defaultdict
import operator

tree = defaultdict(list)
INT_MAX = 10000


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


def pointIsInPolygon(pol, p):
    extreme = Point(INT_MAX, p.y)
    count = index = 0
    while True:
        next = (index + 1) % len(pol)
        if theyIntersect(pol[index], pol[next], p, extreme):
            if theOrientation(pol[index], p, pol[next]) == 0:
                return onSegment(pol[index], p, pol[next])
        count += 1
        index = next
        if index == 0:
            break
    k = (count % 2 == 1)
    return k


def theyIntersect(a, b, c, d):
    o1 = theOrientation(a, b, c)
    o2 = theOrientation(a, b, d)
    o3 = theOrientation(c, d, a)
    o4 = theOrientation(c, d, b)

    if o1 != o2 and o3 != o4 or (o1 == 0 and onSegment(a, c, b)) or (o2 == 0) and (onSegment(a, d, b)) or (o3 == 0) and (onSegment(c, a, d)) or (o4 == 0 and onSegment(c, b, d)):
        return True
    return False


def theOrientation(p, q, r):
    val = (((q.y - p.y) *
            (r.x - q.x)) -
           ((q.x - p.x) *
            (r.y - q.y)))
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def onSegment(p, q, r):
    if ((q.x <= max(p.x, r.x)) &
            (q.x >= min(p.x, r.x)) &
            (q.y <= max(p.y, r.y)) &
            (q.y >= min(p.y, r.y))):
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

