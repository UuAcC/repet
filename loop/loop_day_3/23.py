def f(n):
    if n > 8:
        return 0
    elif n == 8:
        return 1
    else:
        return f(n * 2) + f(n + 1)


def g(n):
    if n > 15:
        return 0
    elif n == 15:
        return 1
    else:
        return g(n * 2) + g(n + 1)


print(f(4) * g(10))