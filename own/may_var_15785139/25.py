def f(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                res.append(i)
            if n // i != i and n // i % 2 == 0:
                res.append(n // i)
    return res


for i in range(110203, 110246):
    r = f(i)
    if len(r) == 4:
        print(r)