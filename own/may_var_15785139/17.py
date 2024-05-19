f = [int(x) for x in open('17.txt').readlines()]
c = 0
m = 0
for i in range(len(f) - 1):
    for j in range(i + 1, len(f)):
        if ((f[i] + f[j]) % 80 == 0) and ((f[i] % 50 == 0) or (f[j] % 50 == 0)):
            c += 1
            m = max(m, f[i] + f[j])
print(c, m)