f = open('26.txt')
n = f.readline()
a = [int(x) for x in f]
a.sort(reverse=True)
res = []
prev = 1000000000
for x in a:
    if prev - x >= 8:
        res.append(x)
        prev = x
print(len(res), res[-1])
