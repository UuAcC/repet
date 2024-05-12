from sys import setrecursionlimit


def f(x):
    res = 0
    while x > 0:
        if x % 27 > 9:
            res += 1
        x //= 27
    return res

print()