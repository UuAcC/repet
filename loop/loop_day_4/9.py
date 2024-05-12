f = open('9.txt')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    if (a[0] + a[1] == a[2] + a[3]) or (a[0] + a[2] == a[1] + a[3]) or (a[0] + a[3] == a[2] + a[1]):
        if sum(a) - max(a) > 0:
            if sum(a) % 2 == 0:
                c += 1
print(c)
