f = open('17.txt')
n = int(f.readline())
a = [int(x) for x in f]
m_19 = 1000000000000000
c = 0
m = 0
for x in a:
    if x % 19 == 0:
        m_19 = min(m_19, x)
for i in range(n - 1):
    if a[i] > m_19 or a[i + 1] > 19:
        c += 1
        m = max(m, a[i] + a[i + 1])
print(c, m)