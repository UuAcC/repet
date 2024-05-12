f = open('26.txt')
A = []
B = []
c_A = 0
n, m = [int(x) for x in f.readline().split()]
for s in f:
    s = s.split()
    if s[-1] == 'A':
        A.append([int(s[0]), int(s[1])])
    else:
        B.append([int(s[0]), int(s[1])])
A.sort()
B.sort()
for b in B:
    if (m - (b[0] * b[1])) > 0:
        m -= b[0] * b[1]
    else:
        m -= (m // b[0]) * b[0]
if m > 0:
    for a in A:
        if (m - (a[0] * a[1])) > 0:
            c_A += a[1]
            m -= a[0] * a[1]
        else:
            c_A += (m // a[0])
            m -= (m // a[0]) * a[0]
print(c_A, m)