def f(n):
    if n > 10:
        return 0
    elif n == 10:
        return 1
    return f(n + 1) + f(n + 2) + f(n * 3)


print(f(1))