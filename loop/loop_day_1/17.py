f = open('17.txt')
a = [int(x) for x in f]
c = 0
res = -(10 ** 8)
for i in range(10000-1):
    for j in range(i, 10000):
        if ((a[i] % 19 == 0) or (a[j] % 19 == 0)) and ((a[i] - a[j]) % 2 == 0):
            c += 1
            res = max(res, a[i] + a[j])
print(c, res)