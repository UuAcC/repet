f = open('33105.txt')
n = int(f.readline())
res = 0
more = []
m = 0
for x in f:
    s = int(x)
    if s <= 100:
        res += s
    else:
        more.append(s)
more.sort()
for x in range(len(more)):
    if x < len(more) // 2:
        res += more[x] * 0.7
        m = more[x]
    else:
        res += more[x]
print(res // 1 + 1, m)