f = open('9.txt')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort(reverse=True)
    if a[1] - a[5] == 20:
        c += 1
print(c)