# -*- coding: utf-8 -*-


class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord


# def semelhantesLLL(a, b, p1, p2):
def getABC(a, b, p):
    u = [a.x - b.x, a.y - b.y]  # AB
    v = [a.x - p.x, a.y - p.y]  # AC
    w = [b.x - p.x, b.y - p.y]  # BC

    return [u, v, w]


def semelhantes(t1, t2):
    a = [t1[0][0]/t2[0][0], 0]
    b = [t1[1][0]/t2[1][0], t1[1][1]/t2[1][1]]
    c = [t1[2][0]/t2[2][0], t1[2][1]/t2[2][1]]
    if a[0] == b[0] and b[0] == c[0]:
        if a[1] == b[1] and b[1] == c[1]:
            return True
    return False


def solve(a, b, pts):
    answer = 1
    tree = []
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i == j:
                continue
            triangle_1 = getABC(a, b, pts[i])
            triangle_2 = getABC(a, b, pts[j])

            if semelhantes(triangle_1, triangle_2):
                tree.append(triangle_1)
                tree.append(triangle_2)
                answer += 2
                if triangle_2 in tree and i > 0:
                    answer -= 1
    return answer


if __name__ == "__main__":
    P, Xa, Xb = map(int, input().split(" "))
    points = []

    # Ancoras
    A = Point(Xa, 0)
    B = Point(Xb, 0)

    for point in range(P):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))

    # Primeira abordagem: calculo a semelhança entre os triângulos
    # Pela relação AB/DE = BC/EF = CA/FD
    # Comparo par a par
    # Caclular a semelhança é linear, comparar não
    print(solve(A, B, points))
