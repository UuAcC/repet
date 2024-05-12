f = open('17.txt')
s = [int(x) for x in f]
m_s = 0
c = 0
for i in range(len(s) - 2):
    ss = [s[i] ** 2, s[i + 1] ** 2, s[i + 2] ** 2]
    if (s[i] > 0) and (s[i + 1] > 0) and (s[i + 2] > 0):
        m = max(ss)
        if (sum(ss) - m) > m:
            c += 1
            m_s = max(m_s, s[i] + s[i + 1] + s[i + 2])
print(c, m_s)