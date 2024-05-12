def dels(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for x in range(35_000_000, 40_000_000):
    res = x
    while res % 2 == 0:
        res //= 2
    n = round(res ** 0.25)
    if dels(n) and n ** 4 == res:
        print(x)

