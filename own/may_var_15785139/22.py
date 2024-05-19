f = open('22.txt')
D = dict()
c = 0
D[0] = 0
flag = True
while flag:
    flag = False
    for s in f:
        ID, T, *a = [int(x) for x in s.split()]
        if ID in D:
            continue
        fl = True
        start = 0
        for x in a:
            if x not in D:
                fl = False
                break
            start = max(start, D[x])
        if fl:
            D[ID] = start + T
            if D[ID] <= 170:
                c += 1
            flag = True
print(c)