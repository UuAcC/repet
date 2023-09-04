a = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3:]
    else:
        ost = (n % 3) * 3
        s += bin(ost)[2:]
    r = int(s, 2)
    if r > 151:
        a.append(r)
print(min(a))
