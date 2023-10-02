def f(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


print(f(2023) / f(2020))
