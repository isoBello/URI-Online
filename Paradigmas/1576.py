# -*- coding: utf-8 -*-
class Building:
    def __init__(self, x, y, z):
        self.left = x
        self.height = y
        self.right = z


def solve(building, left, right):
    if left == right:
        view = [[building[left].left, building[left].height], [building[left].right, 0]]
        return view

    mid = (left + right) // 2
    f_build = solve(building, left, mid)
    s_build = solve(building, mid + 1, right)

    return merge(f_build, s_build)


def merge(A, B):
    skyline = []
    i, j = 0, 0
    h1, h2 = 0, 0
    while (i < len(A)) and (j < len(B)):
        if A[i][0] < B[j][0]:
            x, h1 = A[i][0], A[i][1]
            skyline = append(skyline, [x, max(h1, h2)])
            i += 1
        elif A[i][0] == B[j][0]:
            h1, h2 = A[i][1], B[j][1]
            x = A[i][0]
            skyline = append(skyline, [x, max(h1, h2)])
            i += 1
            j += 1
        else:
            h2, x = B[j][1], B[j][0]
            skyline = append(skyline, [x, max(h1, h2)])
            j += 1
    skyline = check_integrality(skyline, i, j, A, B)
    return skyline


def check_integrality(ans, i, j, l1, l2):
    ans.extend(l1[i:])
    ans.extend(l2[j:])
    return ans


def append(S, llist):
    n = len(S)
    if n > 0 and S[n - 1][0] == llist[0]:
        S[n - 1][1] = max(S[n - 1][1], llist[1])
        return S
    elif n > 0 and S[n - 1][1] == llist[1]:
        return S
    S.append(llist)
    return S


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
            buildings.append(Building(L, H, R))
        except (EOFError, ValueError) as e:
            break

    answer = solve(buildings, 0, len(buildings) - 1)
    print_skyline(answer)

