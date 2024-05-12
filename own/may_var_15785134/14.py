def f(n):
    s = ''
    while n >= 5:
        s += str(n % 5)
        n //= 5
    s += str(n)
    return s[::-1]


print(f(125 + 25 ** 3 + 5 ** 9))