f = open('17.txt')
m_21 = 0
m_s = 1000000000000
c = 0
a = [int(x) for x in f]
for x in a:
    if x % 21 == 0:
        m_21 = max(m_21, x)
for i in range(10000-1):
    s = a[i] + a[i + 1]
    if a[i] > m_21 or a[i + 1] > m_21:
        c += 1
        m_s = min(s, m_s)
print(c, m_s)