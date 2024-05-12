f = open('26.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()
c = 0
prev = 0
for i in range(len(a)):
    if a[i] >= prev * 1.1:
        c += 1
        prev = a[i]
print(c, prev)