f = open('68510.txt')
c = 0
for s in f:
    a1, a2, a3, a4 = [int(x) for x in s.split()]
    m = max(a1, a2, a3, a4)
    if m < sum([a1, a2, a3, a4]) - m:
        if (a1 + a2 == a3 + a4) or (a3 + a2 == a1 + a4) or (a4 + a2 == a3 + a1):
            c += 1
print(c)