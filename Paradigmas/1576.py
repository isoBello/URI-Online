# -*- coding: utf-8 -*-
def solve(builds):
    if len(builds) == 1:
        return [[builds[0][0], builds[0][1]],
                [builds[0][2], 0]]

    mid = len(builds) // 2
    left = solve(builds[:mid])
    right = solve(builds[mid:])
    return merge(left, right)


def merge(A, B):
    hA, hB = 0, 0
    i, j = 0, 0
    fly_path = []

    while i < len(A) and j < len(B):
        if A[i][0] < B[j][0]:
            hA, x = A[i][1], A[i][0]
            i += 1
        elif B[j][0] < A[i][0]:
            hB, x = B[j][1], B[j][0]
            j += 1
        else:
            hA, hb = A[i][1], B[j][1]
            x = B[j][0]
            i += 1
            j += 1

        top = max(hA, hB)
        condition = check_top(fly_path, top)
        if condition:
            fly_path.append([x, top])

    fly_path = check_remains(fly_path, A, B, i, j)
    return fly_path


def check_remains(llist, a, b, i, j):
    if i < len(a):
        llist.extend(a[i:])
    if j < len(b):
        llist.extend(b[j:])
    return llist


def check_top(list, at_top):
    if list:
        if list[-1][1] != at_top:
            return True
    return not list


def print_skyline(S):
    output = ''
    for i in range(len(S)):
        a, b = str(S[i][0]), str(S[i][1])
        if i == 0:
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

    skyline = solve(buildings)
    print_skyline(skyline)


