f = open('9.txt')
ans = 0
for s in f:
    a = [int(x) for x in s.split()]
    k4 = 0
    k1 = 0
    s4 = 0
    for x in a:
        if a.count(x) == 4:
            k4 += 1
            s4 += x
        elif a.count(x) == 1:
            k1 += 1
    if k4 != 4 and k1 != 1:
        continue
    if 4 * sum(a) > 7 * s4:
        ans += 1
print(ans)
