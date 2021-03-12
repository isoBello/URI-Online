# -*- coding: utf-8 -*-
def solve(B):
    if not B:
        return []
    if len(B) == 1:
        return [[B[0][0], B[0][1]], [B[0][2], 0]]

    mid = len(B) // 2
    left = solve(B[:mid])
    right = solve(B[mid:])
    return merge(left, right)


def merge(A, B):
    hA, hB = 0, 0
    i, j = 0, 0
    skyline = []

    while i < len(A) and j < len(B):
        if A[i][0] < B[j][0]:
            hA, x = A[i][1], A[i][0]
            i += 1
        elif B[j][0] < A[i][0]:
            hB, x = B[j][1], B[j][0]
            j += 1
        else:
            hA, hB = A[i][1], B[j][1]
            x = B[j][0]
            i += 1
            j += 1
        k = max(hA, hB)
        if valid_top(skyline, k):
            skyline.append([x, k])
    skyline.extend(B[j:])
    skyline.extend(A[i:])
    return skyline


def valid_top(llist, k):
    return not llist or llist[-1][1] != k


def print_skyline(S):
    output = ''
    for s in range(len(S)):
        a, b = str(S[s][0]), str(S[s][1])
        if s == 0:
            output += a + " " + b
        else:
            output += " " + a + " " + b
    print(output, end="\n")


if __name__ == "__main__":
    buildings = []

    while True:
        try:
            L, H, R = map(int, input().split(" "))
            buildings.append([L, H, R])
        except (EOFError, ValueError) as e:
            break

    answer = solve(buildings)
    print_skyline(answer)


