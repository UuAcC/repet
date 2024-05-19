# ---------- A ----------

f = open('27-A.txt')
n = int(f.readline())
s = [int(x) for x in f]
m = 0
for a1 in range(n):
    for a2 in range(n):
        for a3 in range(n):
            if (a1 != a2) and (a3 != a2) and (a1 != a3):
                if (s[a1] + s[a2] + s[a3]) % 3 == 0:
                    m = max(m, s[a1] + s[a2] + s[a3])
print(m)

# ---------- B ----------

f = open('27-B.txt')
n = int(f.readline())
s0 = []
s1 = []
s2 = []
m = 0
for i in range(n):
    a = int(f.readline())
    if a % 3 == 0:
        s0.append(a)
    elif a % 3 == 1:
        s1.append(a)
    else:
        s2.append(a)
for s in s0, s1, s2:
    s.sort(reverse=True)
    m = max(m, s[0] + s[1] + s[2])
m = max(m, s0[0] + s1[0] + s2[0])
print(m)
