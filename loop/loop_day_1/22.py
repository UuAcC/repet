f = open('47610.txt')
D = dict()
D[0] = 0
matrix = [x for x in f]
check = True
while check:
    check = False
    for s in matrix:
        ID, T, *a = [int(x) for x in s.split()]
        if ID in D:
            continue
        flag = True
        start = 0
        for x in a:
            if x not in D:
                flag = False
                break
            start = max(start, D[x])
        if flag:
            D[ID] = start + T
            check = True
print(max(D.values()))