f = open('22.txt')
D = dict()
D[0] = 0
fl = True
while fl:
    fl = False
    for s in f:
        ID, T, *a = [int(x) for x in s.split()]
        if ID in D:
            continue
        start = 0
        flag = True
        for x in a:
            if x in D:
                start = max(start, D[x])
            else:
                flag = False
                break
        if flag:
            D[ID] = start + T
            fl = True
print(max(D.values()))