f = open('24.txt').readline()
for e in 'A, E, O, U':
    f = f.replace(e, '1')
for e in 'K, L, M, N':
    f = f.replace(e, '2')
m = 0
temp = 1
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        temp += 1
    else:
        m = max(temp, m)
        temp = 1
print(m)
