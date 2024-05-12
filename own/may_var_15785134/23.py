def F(n):
    if n == 13:
        return 1
    elif n > 13:
        return 0
    else:
        return F(n + 1) + F(n * 2) + F(n * 3)


def N(n):
    if n == 44:
        return 1
    elif n == 29 or n > 44:
        return 0
    else:
        return N(n + 1) + N(n * 2) + N(n * 3)


print(F(2) * N(13))