from sys import setrecursionlimit


def f(n):
    if n <= 12:
        return 1
    return f(n - 1) + n - 2


setrecursionlimit(5000)
print(f(2024) - f(2020))
