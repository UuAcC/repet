f = open('26.txt')
res_c = 0
res_d = 0
n, m = [int(x) for x in f.readline().split()]
Days = {
    1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [],
    12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [],
    22: [], 23: [], 24: [], 25: [], 26: [], 27: [], 28: [], 29: [], 30: [], 31: []
}
for _ in range(m):
    S, D, T, L = [int(x) for x in f.readline().split()]
    E = T + L
    if E > 24:
        Days[D].append([T, 24])
        if D != 31:
            Days[D + 1].append([0, E % 24])
    else:
        Days[D].append([T, E])
for d in Days.keys():
    m_c = 0
    for i in range(1, 25):
        c = 0
        for a in Days[d]:
            if a[0] < i <= a[1]:
                c += 1
        m_c = max(c, m_c)
    if m_c > res_c:
        res_c = m_c
        res_d = d
print(res_c, res_d)
