f = open('24.txt').readline()
m_c = -1
c = 1
for i in range(len(f) - 1):
    if (f[i] == 'X' and f[i + 1] == 'Y') or (f[i] == 'Y' and f[i + 1] == 'Z') or (f[i] == 'Z' and f[i + 1] == 'X'):
        c += 1
    else:
        m_c = max(m_c, c)
        c = 1
print(m_c)