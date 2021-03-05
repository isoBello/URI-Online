# -*- coding: utf-8 -*-
from collections import defaultdict


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


class Graph:
    def __init__(self, N):
        self.vertices = N
        self.edges = defaultdict(list)

    def addEdge(self, u, v):
        self.edges[u].append(v)


def solve(a, b, pts, G):
    for i in range(len(pts)):
        triangle = [a, b, pts[i]]
        for j in range(len(pts)):
            if pts[j] in triangle:
                continue
            if pointIsInside(triangle, pts[j]):
                G.addEdge(i, j)


def pointIsInside(a, b):
    # Area of triangle ABi
    areaABi = area(a[0].x, a[0].y,
                   a[1].x, a[1].y,
                   a[2].x, a[2].y)
    # Area of triangle jBC
    areajBC = area(b.x, b.y,
                   a[1].x, a[1].y,
                   a[2].x, a[2].y
                   )
    # Area of triangle AjC
    areaAjC = area(a[0].x, a[0].y,
                   b.x, b.y,
                   a[2].x, a[2].y)
    # Area of triangle ABj
    areaABj = area(a[0].x, a[0].y,
                   a[1].x, a[1].y,
                   b.x, b.y)

    # If the sum of areajBC, areaAjC and areaABj is same as areaABi
    if areaABi == (areajBC + areaAjC + areaABj):
        return True
    return False


def area(a, b, c, d, e, f):
    return abs((a * (d - f) + c * (f - b)
                + e * (b - d)) / 2.0)


def findLongestPath(G, N):
    M = [0] * (N + 1)
    visited = [False] * (N + 1)

    for i in range(N):
        if not visited[i]:
            DFS(i, G, M, visited)
    answer = 0
    for i in range(N):
        answer = max(answer, M[i])

    return answer + 1


def DFS(node, G, M, visited):
    visited[node] = True
    for u in G.edges[node]:
        if not visited[u]:
            DFS(u, G, M, visited)
        M[node] = max(M[node], 1 + M[u])


if __name__ == "__main__":
    P, Xa, Xb = map(int, input().split(" "))
    points = []

    # Ancoras
    A = Point(Xa, 0)
    B = Point(Xb, 0)
    graph = Graph(P)

    for point in range(P):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))

    solve(A, B, points, graph)
    print(findLongestPath(graph, P))
