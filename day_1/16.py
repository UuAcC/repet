def F(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


print(F(2023) / F(2020))
