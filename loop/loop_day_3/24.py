f = open('24.txt').readline()
for i in ['6', '7', '8', '9']:
    f = f.replace(i, '2')
for i in ['A', 'B', 'C']:
    f = f.replace(i, '1')
m = 0
temp = 1
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        temp += 1
    else:
        m = max(temp, m)
        temp = 1
print(m)