a = open('24.txt').readline()
# m_c = 0
# c = 1
# for i in range(len(a) - 1):
#     if (a[i] == "B" and a[i + 1] == "A") or (a[i] == "A" and a[i + 1] == "B"):
#         c += 1
#     else:
#         m_c = max(m_c, c)
#         c = 1
# print(m_c)
m_c = 0
a = list(a.replace('AB', '11'))
b = a.copy()
for i in range(len(a) - 1):
    if a[i] == '1' and a[i + 1] == 'A':
        b[i + 1] = '1   '
b = ''.join(b)
for e in 'ABC':
    b = b.replace(e, ' ')
b = b.split()
for s in b:
    m_c = max(m_c, len(s))
print(m_c)