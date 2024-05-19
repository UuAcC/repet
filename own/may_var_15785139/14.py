n = 9 ** 7 + 3 ** 21 - 9
c = 0
while n % 3 != n:
    if n % 3 == 2:
        c += 1
    n //= 3
print(c)