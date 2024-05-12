def f(x, y, prev):
    if x > y:
        return 0
    if x == y:
        return 1
    if prev == 0:
        return f(x + 1, y, 0) + f(x + 2, y, 0) + f(x * 2, y, 1)
    else:
        return f(x + 1, y, 0) + f(x + 2, y, 0)


print(f(1, 11, 0))
