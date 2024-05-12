print('k l m n')
for k in 0,1:
    for l in 0,1:
        for m in 0,1:
            for n in 0,1:
                f = (not n) or (k and (not m)) or (l == m)
                if not f:
                    print(k, l, m, n)