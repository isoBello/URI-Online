# -*- coding: utf-8 -*-
class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord

    def getX(self):
        return self.x

    def getY(self):
        return self.y


if __name__ == "__main__":
    P, Xa, Xb = map(int, input().split(" "))
    points = []

    for point in range(P):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))


