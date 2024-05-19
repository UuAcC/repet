f = open('26.txt')
s, n = [int(x) for x in f.readline().split()]
a = [int(x) for x in f]
a.sort()
c = 0
IDs = []
Xs = []
for i in range(n):
    if a[i] <= s:
        IDs.append(i)
        Xs.append(a[i])
        s -= a[i]
        c += 1
s += Xs[-1]
del Xs[-1]
m = 0
for i in range(IDs[-1], n):
    if a[i] <= s:
        m = max(m, a[i])
print(c, m)