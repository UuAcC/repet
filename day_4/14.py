x = 4 ** 511 + 2 ** 511 - 511
s = bin(x)[2:]
print(s.count('1'))


x = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
s = set()
while x > 0:
    s.add(x % 6)
    x //= 6
print(len(s))
