f = open('17.txt')
a = [x for x in f]
m_2 = '10000000'
c = 0
mm = 10000000000000
for s in a:
    if 9 < int(s) < 100:
        m_2 = str(min(int(s), int(m_2)))
for x in range(len(a) - 1):
    if (m_2 not in a[x]) or (m_2 not in a[x + 1]):
        c += 1
        mm = min(mm, abs(int(a[x]) - int(a[x - 1])))
print(c, mm)