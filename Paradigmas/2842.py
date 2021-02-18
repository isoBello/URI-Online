# -*- coding: utf-8 -*-

# Solving Dabriel e Suas Strings
def concatenar(a, b):
    if len(a) > len(b):
        if b in a:
            new = a
        else:
            new = b + a
            new = "".join(list(dict.fromkeys(new)))
    else:
        if a in b:
            new = b
        else:
            new = a + b
            new = "".join(list(dict.fromkeys(new)))

    print(new, len(new))


if __name__ == "__main__":
    A = input()
    B = input()

    concatenar(A, B)
